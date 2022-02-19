import os
import img2pdf
from PIL import Image 
from natsort import natsorted
import shutil

## 【使い方】
##  0. pdf化する画像のバックアップをとる!
##  1. fromフォルダにpdf化したい画像を入れる。
##     画像ファイルの名前はページ順に、自然数の順で名付ける。
##　　　サポートしているファイル形式：jpg、pdf、webp
##  2. コマンドラインで、"python3 webp2pdf.py"と入力し、実行。
##  3. output.pdfが出力される
##     注意：fromフォルダの画像は全消去されるので、必ずバックアップをとっておくこと！

if __name__ == '__main__':
    pdf_FileName = "./output.pdf" 
    jpg_Folder = "./to/" 
    webp_Folder = "./from/"
    
    os.mkdir("./to")

    cnt = 1
    hoge = os.listdir(webp_Folder)
    hoge = natsorted(hoge)
    for j in hoge :
        if j.endswith(".webp") or j.endswith(".WEBP") or \
           j.endswith(".png") or j.endswith(".PNG") or \
           j.endswith(".jpg") or j.endswith(".JPG") or \
           j.endswith(".jpeg") or j.endswith(".JPEG") :
            im = Image.open(webp_Folder + j).convert("RGB")
            im.save(jpg_Folder + str(cnt) + ".jpg", "jpeg")
            cnt = cnt+1
            
    with open(pdf_FileName,"wb") as f:
        fuga = os.listdir(jpg_Folder) 
        fuga = natsorted(fuga)
        f.write(img2pdf.convert([Image.open(jpg_Folder+j).filename for j in fuga if j.endswith(".jpg")]))

    shutil.rmtree(jpg_Folder)
    shutil.rmtree(webp_Folder)
    os.mkdir("./from")
