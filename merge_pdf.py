"""
This application merges all pdf within this folder to an output pdf files.
1. List down all the pdfs in the working folder.
2. PdfFileMerge initialised.
3. Merger appends the file content in memory.
4. write to output file.
"""
import os
from PyPDF2 import PdfFileMerger, PdfFileReader

filelist = [a for a in os.listdir() if a.endswith(".pdf")]

# list down for checking list of pdf to merge.
print(filelist)

merger = PdfFileMerger()

for pdf in filelist:
    with open(pdf, 'rb') as source:
        tmp = PdfFileReader(source)
        merger.append(tmp)

# to rename the pdf file after executing.
OUTPUT_FILE="output-final.pdf"
with open(OUTPUT_FILE, "wb") as fout:
    merger.write(fout)
