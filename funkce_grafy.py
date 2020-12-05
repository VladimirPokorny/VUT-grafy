import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

#initial commit

def graf_proudy_moment_otacky(tb_t, tb_i1, tb_i2, tb_M, tb_n,file,rozsah1,rozsah2):
    table = pd.read_csv(file)

    t = table.iloc[rozsah1:rozsah2, tb_t]
    t = t.astype(np.float)

    i1 = table.iloc[rozsah1:rozsah2, tb_i1]
    i1 = i1.astype(np.float)

    if tb_i2 != -1:
        i2 = table.iloc[rozsah1:rozsah2, tb_i2]
        i2 = i2.astype(np.float)
        i3 = - i1 - i2

    M = table.iloc[rozsah1:rozsah2, tb_M]
    M = M.astype(np.float)

    n = table.iloc[rozsah1:rozsah2, tb_n]
    n = n.astype(np.float)

    plt.figure(figsize=(15, 15))

    plt.subplot(2, 1, 1)
    plt.title('Průběhy proudů, otáček a momentu \nData ze souboru: ' + os.path.basename((file).replace('.csv', '')))
    plt.plot(t, i1, )
    if tb_i2 != -1:
        plt.plot(t, i2, )
        plt.plot(t, i3, )
    plt.grid(color='grey', linestyle='-', linewidth=0.1)
    plt.ylabel('I [A]')

    color = 'tab:red'
    ax1 = plt.subplot(2, 1, 2)
    ax1.set_xlabel('t [s]')
    ax1.set_ylabel('M [Nm]', color=color)
    ax1.plot(t, M, color=color)
    ax1.tick_params(axis='y', labelcolor=color)
    plt.grid(color='grey', linestyle='-', linewidth=0.1)

    color = 'tab:blue'
    ax2 = ax1.twinx()
    ax2.set_ylabel('n [ot/min]', color=color)  # we already handled the x-label with ax1
    ax2.plot(t, n * 50, color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    # plt.show()

    plt.rcParams['pdf.fonttype'] = 42
    file = os.path.basename((file).replace('.csv', ''))
    plt.savefig('pdf/' + file + '.pdf', bbox_inches='tight')
    plt.close()
    return 1

def graf_otacky_na_Momentu(tb_M, tb_n,file,rozsah1,rozsah2):
    table = pd.read_csv(file)

    M = table.iloc[rozsah1:rozsah2, tb_M]
    M = M.astype(np.float)

    n = table.iloc[rozsah1:rozsah2, tb_n]
    n = n.astype(np.float)

    plt.figure(figsize=(15, 15))

    plt.plot(M, n * 50, )
    plt.title('Závislost otáček na momentu \n Data ze souboru: ' + os.path.basename((file).replace('.csv', '')))
    plt.grid(color='grey', linestyle='-', linewidth=0.1)
    plt.xlabel('M [Nm]')
    plt.ylabel('n [ot/min]')

    plt.rcParams['pdf.fonttype'] = 42
    file = os.path.basename((file).replace('.csv', ''))
    plt.savefig('pdf/' + file + '_torqueRPM.pdf', bbox_inches='tight')
    plt.close()
    return 1