import matplotlib.pyplot as plt
#from PyPDF2 import PdfFileReader, PdfFileMerger
import pandas as pd
import numpy as np
import glob
import natsort

t = []
i1 = []
i2 = []
i3 = []
M = []
n = []

files = glob.glob("mereni/t_i1_i2_n_M/*.csv")
files = natsort.natsorted(files,reverse=False)
print(files)

for file in files:                   # iterate over the list of files

    table = pd.read_csv (file)

    rozsah1 = 3
    rozsah2 = len(table.loc[:, 'x-axis'])

    t = table.iloc[rozsah1:rozsah2, 0]
    t = t.astype(np.float)

    i1 = table.iloc[rozsah1:rozsah2, 1]
    i1 = i1.astype(np.float)

    i2 = table.iloc[rozsah1:rozsah2, 2]
    i2 = i2.astype(np.float)

    i3 = - i1 -i2

    M = table.iloc[rozsah1:rozsah2, 4]
    M = M.astype(np.float)

    n = table.iloc[rozsah1:rozsah2, 3]
    n = n.astype(np.float)

    plt.figure(figsize=(15, 15))
    plt.title('Data ze souboru: ' + file)

    plt.subplot(3, 1, 1)
    plt.plot(t, i1, )
    plt.plot(t, i2, )
    plt.plot(t, i3, )
    plt.grid(color='grey', linestyle='-', linewidth=0.1)
    plt.ylabel('I [A]')

    plt.subplot(3, 1, 2)
    plt.plot(t, M, )
    plt.grid(color='grey', linestyle='-', linewidth=0.1)
    plt.ylabel('M [Nm]')

    plt.subplot(3, 1, 3)
    plt.plot(t, n*50, )
    plt.grid(color='grey', linestyle='-', linewidth=0.1)
    plt.xlabel('t (s)')
    plt.ylabel('n [ot/min]')

    # plt.show()

    plt.rcParams['pdf.fonttype'] = 42
    plt.savefig('pdf/' + file.replace('mereni/t_i1_i2_M_n\\','') + '.pdf', bbox_inches='tight')
    # plt.close()

files = glob.glob("mereni/t_i1_i2_M/*.csv")
files = natsort.natsorted(files,reverse=False)
print(files)

for file in files:                   # iterate over the list of files

    table = pd.read_csv (file)

    rozsah1 = 3
    rozsah2 = len(table.loc[:, 'x-axis'])

    t = table.iloc[rozsah1:rozsah2, 0]
    t = t.astype(np.float)

    i1 = table.iloc[rozsah1:rozsah2, 1]
    i1 = i1.astype(np.float)

    i2 = table.iloc[rozsah1:rozsah2, 2]
    i2 = i2.astype(np.float)

    i3 = - i1 -i2

    M = table.iloc[rozsah1:rozsah2, 3]
    M = M.astype(np.float)

    plt.figure(figsize=(15, 15))
    plt.title('Data ze souboru: ' + file)

    plt.subplot(3, 1, 1)
    plt.plot(t, i1, )
    plt.plot(t, i2, )
    plt.plot(t, i3, )
    plt.grid(color='grey', linestyle='-', linewidth=0.1)
    plt.ylabel('I [A]')

    plt.subplot(3, 1, 2)
    plt.plot(t, M, )
    plt.grid(color='grey', linestyle='-', linewidth=0.1)
    plt.ylabel('M [Nm]')

    plt.subplot(3, 1, 3)
    #plt.plot(t, n*50, )
    plt.xlabel('t (s)')
    plt.grid(color='grey', linestyle='-', linewidth=0.1)
    plt.ylabel('n [ot/min]')

    # plt.show()

    plt.rcParams['pdf.fonttype'] = 42
    plt.savefig('pdf/' + file.replace('mereni/t_i1_i2_M\\','') + '.pdf', bbox_inches='tight')
    # plt.close()

files = glob.glob("mereni/t_i1_M_n_i2/*.csv")
files = natsort.natsorted(files,reverse=False)
print(files)

for file in files:                   # iterate over the list of files

    table = pd.read_csv (file)

    rozsah1 = 3
    rozsah2 = len(table.loc[:, 'x-axis'])

    t = table.iloc[rozsah1:rozsah2, 0]
    t = t.astype(np.float)

    i1 = table.iloc[rozsah1:rozsah2, 1]
    i1 = i1.astype(np.float)

    i2 = table.iloc[rozsah1:rozsah2, 4]
    i2 = i2.astype(np.float)

    i3 = - i1 -i2

    M = table.iloc[rozsah1:rozsah2, 2]
    M = M.astype(np.float)

    n = table.iloc[rozsah1:rozsah2, 3]
    n = n.astype(np.float)

    plt.figure(figsize=(15, 15))
    plt.subplot(3, 1, 1)
    plt.title('Data ze souboru: ' + file)
    plt.plot(t, i1, )
    plt.plot(t, i2, )
    plt.plot(t, i3, )
    plt.grid(color='grey', linestyle='-', linewidth=0.1)
    plt.ylabel('I [A]')

    plt.subplot(3, 1, 2)
    plt.plot(t, M, )
    plt.grid(color='grey', linestyle='-', linewidth=0.1)
    plt.ylabel('M [Nm]')

    plt.subplot(3, 1, 3)
    plt.plot(t, n*50, )
    plt.xlabel('t (s)')
    plt.grid(color='grey', linestyle='-', linewidth=0.1)
    plt.ylabel('n [ot/min]')

    # plt.show()

    plt.rcParams['pdf.fonttype'] = 42
    plt.savefig('pdf/' + file.replace('mereni/t_i1_M_n_i2\\','') + '.pdf', bbox_inches='tight')
   # plt.close()

files = glob.glob("mereni/t_i1_M_n/*.csv")
files = natsort.natsorted(files,reverse=False)
print(files)

for file in files:                   # iterate over the list of files

    table = pd.read_csv (file)

    rozsah1 = 3
    rozsah2 = len(table.loc[:, 'x-axis'])

    t = table.iloc[rozsah1:rozsah2, 0]
    t = t.astype(np.float)

    i1 = table.iloc[rozsah1:rozsah2, 1]
    i1 = i1.astype(np.float)

    M = table.iloc[rozsah1:rozsah2, 2]
    M = M.astype(np.float)

    n = table.iloc[rozsah1:rozsah2, 3]
    n = n.astype(np.float)

    plt.figure(figsize=(15, 15))
    plt.subplot(3, 1, 1)
    plt.title('Data ze souboru: ' + file)
    plt.plot(t, i1, )
    plt.grid(color='grey', linestyle='-', linewidth=0.1)
    plt.ylabel('I [A]')

    plt.subplot(3, 1, 2)
    plt.plot(t, M, )
    plt.grid(color='grey', linestyle='-', linewidth=0.1)
    plt.ylabel('M [Nm]')

    plt.subplot(3, 1, 3)
    plt.plot(t, n*50, )
    plt.xlabel('t (s)')
    plt.grid(color='grey', linestyle='-', linewidth=0.1)
    plt.ylabel('n [ot/min]')

    # plt.show()

    plt.rcParams['pdf.fonttype'] = 42
    plt.savefig('pdf/' + file.replace('mereni/t_i1_M_n\\','') + '.pdf', bbox_inches='tight')
    plt.close()