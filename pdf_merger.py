from PyPDF2 import PdfFileReader, PdfFileMerger
import glob
import natsort

# commit n2

pdfs = glob.glob("pdf/*.pdf")  # get all the .txt files
pdfs = natsort.natsorted(pdfs,reverse=False)
print(pdfs)

merger = PdfFileMerger()

for pdf in pdfs:  # iterate over the list of files
   merger.append(PdfFileReader(pdf),'rb')

merger.write("Vsechny_grafy.pdf")
merger.close()