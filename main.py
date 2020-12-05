import pandas as pd
import glob
import natsort
from funkce_grafy import graf_proudy_moment_otacky, graf_otacky_na_Momentu
from PyPDF2 import PdfFileReader, PdfFileMerger

#initial commit

t = []
i1 = []
i2 = []
i3 = []
M = []
n = []

################################################
files = glob.glob("mereni/t_i1_i2_n_M/*.csv")

files = natsort.natsorted(files,reverse=False)
print(files)

for file in files:                   # iterate over the list of files

   rozsah1 = 3
   rozsah2 = len(pd.read_csv(file).loc[:, 'x-axis'])

   graf_proudy_moment_otacky(0,1,2,4,3,file,rozsah1,rozsah2)   #tb_t, tb_i1, tb_i2, tb_M, tb_n,file,rozsah1,rozsah2
   graf_otacky_na_Momentu(4, 3, file, rozsah1, rozsah2)        #tb_M, tb_n,file,rozsah1,rozsah2

################################################

################################################
files = glob.glob("mereni/t_i1_M_n/*.csv")

files = natsort.natsorted(files,reverse=False)
print(files)

for file in files:                   # iterate over the list of files

   rozsah1 = 3
   rozsah2 = len(pd.read_csv(file).loc[:, 'x-axis'])

   graf_proudy_moment_otacky(0,1,-1,2,3,file,rozsah1,rozsah2)   #tb_t, tb_i1, tb_i2, tb_M, tb_n,file,rozsah1,rozsah2
   graf_otacky_na_Momentu(2, 3, file, rozsah1, rozsah2)        #tb_M, tb_n,file,rozsah1,rozsah2
################################################

################################################
files = glob.glob("mereni/t_i1_M_n_i2/*.csv")

files = natsort.natsorted(files,reverse=False)
print(files)

for file in files:                   # iterate over the list of files

   rozsah1 = 3
   rozsah2 = len(pd.read_csv(file).loc[:, 'x-axis'])

   graf_proudy_moment_otacky(0,1,4,2,3,file,rozsah1,rozsah2)   #tb_t, tb_i1, tb_i2, tb_M, tb_n,file,rozsah1,rozsah2
   graf_otacky_na_Momentu(2, 3, file, rozsah1, rozsah2)        #tb_M, tb_n,file,rozsah1,rozsah2
################################################

################################################
files = glob.glob("mereni/t_i1_i2_M/*.csv")

files = natsort.natsorted(files,reverse=False)
print(files)

for file in files:                   # iterate over the list of files

   rozsah1 = 3
   rozsah2 = len(pd.read_csv(file).loc[:, 'x-axis'])

   graf_proudy_moment_otacky(0,1,2,3,3,file,rozsah1,rozsah2)   #tb_t, tb_i1, tb_i2, tb_M, tb_n,file,rozsah1,rozsah2
   #graf_otacky_na_Momentu(4, 3, file, rozsah1, rozsah2)        #tb_M, tb_n,file,rozsah1,rozsah2
################################################

pdfs = glob.glob("pdf/*.pdf")  # get all the .txt files
pdfs = natsort.natsorted(pdfs,reverse=False)
print(pdfs)

merger = PdfFileMerger()

for pdf in pdfs:  # iterate over the list of files
   merger.append(PdfFileReader(pdf),'rb')

merger.write("Vsechny_grafy.pdf")
merger.close()