import os
import re
import fitz
import docx
import time
import shutil
from glob import glob
import win32com.client as win32
from win32com.client import constants

file_count=0
t1=time.perf_counter()

def save_as_docx(path):
    word = win32.gencache.EnsureDispatch('Word.Application')
    path = path.replace("docs\\","")
    doc = word.Documents.Open(os.path.abspath(os.path.join("docs/", path)))
    doc.Activate ()

    new_file_abs = os.path.abspath(os.path.abspath(os.path.join("docs/", path)))
    new_file_abs = re.sub(r'\.\w+$', '.docx', new_file_abs)

    word.ActiveDocument.SaveAs(
        new_file_abs, FileFormat=constants.wdFormatXMLDocument
    )
    doc.Close(False)

def clean_directory(path):
    for filename in os.listdir(path):
        if filename.endswith(".doc") or filename.endswith(".DOC"):
            filepath = os.path.abspath(os.path.join(path, filename))
            try:
                shutil.rmtree(filepath)
            except OSError:
                os.remove(filepath)

for filename in os.listdir("docs/"):
    print('-'*50)
    print("Processing file: ",filename)
    file_count+=1

    if filename.endswith(".pdf") or filename.endswith(".PDF"):
        with fitz.open(os.path.abspath(os.path.join("docs/", filename))) as f:
            text = ""
            for page in f:
                text += page.get_text()
        output_filename = re.sub("pdf", "txt", filename)

    if filename.endswith(".docx") or filename.endswith(".DOCX") or filename.endswith(".doc") or filename.endswith(".DOC"):
        if filename.endswith(".doc") or filename.endswith(".DOC"):
            paths = glob('docs/*.doc', recursive=True)
            for path in paths:
                save_as_docx(path)
            clean_directory("docs/")

        else:
            pass
        doc = docx.Document(os.path.abspath(os.path.join("docs/", filename)))
        fulltext = []
        for para in doc.paragraphs:
            fulltext.append(para.text)
        text = ''.join(fulltext)
        output_filename = re.sub("(docx?)", "txt", filename)


    if filename.endswith(".txt") or filename.endswith(".TXT"):
        with open(os.path.abspath(os.path.join("docs/", filename))) as f:
            data = f.read()
        text = re.findall("[aA-zZ]+", data)
        output_filename = filename

    with open(os.path.abspath(os.path.join("txt_files/", output_filename)), 'w',encoding="utf-8") as f:
        f.writelines(text)
        f.close()

print("\n")
print('*-'*25)
print("\nCOMPLETED...")
print('*-'*25)
t2=time.perf_counter()
t=t2-t1
if file_count==1:
    print("-"*40)
    print("\nProcessed ",file_count," document")
    print("\nExecution Time: ",t,"seconds.\n")
    print("-"*40)
else:
    print("-"*40)
    print("\nProcessed ",file_count," documents")
    print("\nExecution Time: ",t,"seconds.\n")
    print("-"*40)
