import os
import img2pdf
from PIL import Image 
from natsort import natsorted

if __name__ == '__main__':
    pdf_FileName = "./output.pdf" 
    jpg_Folder = "./jpg/" 
    webp_Folder = "./webp/"
    
    cnt = 1
    hoge = os.listdir(webp_Folder)
    hoge = natsorted(hoge)
    for j in hoge :
        if j.endswith(".webp") :
            im = Image.open(webp_Folder + j).convert("RGB")
            im.save(jpg_Folder + str(cnt) + ".jpg", "jpeg")
            cnt = cnt+1
            
    with open(pdf_FileName,"wb") as f:
        fuga = os.listdir(jpg_Folder) 
        fuga = natsorted(fuga)
        f.write(img2pdf.convert([Image.open(jpg_Folder+j).filename for j in fuga if j.endswith(".jpg")]))
