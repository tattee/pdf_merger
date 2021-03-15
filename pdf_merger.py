from PyPDF2 import PdfFileMerger
import os, sys, glob

def main(pdf_dir):
    os.chdir(pdf_dir)
    filelist = glob.glob("*.pdf") # フォルダ内のpdfリストを取得

    merger = PdfFileMerger()

    for file in filelist:
        merger.append(file)
    # merged.pdfとして保存する
    merger.write('merged.pdf')
    merger.close()

if __name__ == "__main__":
    pdf_dir = sys.argv[1] # フォルダを引数として渡す
    main(pdf_dir)