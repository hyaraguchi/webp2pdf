import os
import img2pdf
from PIL import Image 
from natsort import natsorted
import shutil
import cv2

## 【使い方】
##  1.fromフォルダにpdf化したい画像をフォルダごと入れる
## 　（フォルダに入っている画像をまとめてpdf化する。pdfの名前はフォルダの名前と同じものになる）
##     画像ファイルの名前はページ順に、自然数の順で名付ける。
##　　　サポートしているファイル形式：jpg、jpeg、png、webp
##  2. 実行。
##  3. pdf_filesフォルダにpdfがまとめて出力される
## 　（fromフォルダの画像は消去されない。出力を確認後削除すること）
## 

def webp_to_pdf(root_path, file_name):
    pdf_FileName = root_path + "/" + file_name + "/" + file_name + ".pdf" 
    jpg_Folder = root_path + "/" + file_name + "/to/"
    webp_Folder = root_path + "/" + file_name + "/"

    os.mkdir(root_path + "/" + file_name + "/to")

    cnt = 1
    hoge = os.listdir(webp_Folder)
    hoge = natsorted(hoge)
    for j in hoge :
        if j.endswith(".webp") or j.endswith(".WEBP") or \
           j.endswith(".png") or j.endswith(".PNG") or \
           j.endswith(".jpg") or j.endswith(".JPG") or \
           j.endswith(".jpeg") or j.endswith(".JPEG") :
            try:
                im = Image.open(webp_Folder + j).convert("RGB")
            except OSError:
                cvimg = cv2.imread(webp_Folder + j)
                cvimg = cv2.cvtColor(cvimg, cv2.COLOR_BGR2RGB)
                im =  Image.fromarray(cvimg)
            im.save(jpg_Folder + str(cnt) + ".jpg", "jpeg")
            cnt = cnt+1

    with open(pdf_FileName,"wb") as f:
        fuga = os.listdir(jpg_Folder) 
        fuga = natsorted(fuga)
        f.write(img2pdf.convert([Image.open(jpg_Folder+j).filename for j in fuga if j.endswith(".jpg")]))

    shutil.move(pdf_FileName, root_path + "/pdf_files/" + file_name + ".pdf") 

    shutil.rmtree(jpg_Folder)
    #shutil.rmtree(webp_Folder)
    #os.mkdir("./from")

if __name__ == '__main__':
    root_path = "./from" #input()

    os.mkdir(root_path + "/pdf_files")

    if os.path.isdir(root_path):
        dirs = os.listdir(root_path)
        for dir in dirs:
            if (dir != ".DS_Store" and dir != "pdf_files"):
                webp_to_pdf(root_path, dir)

