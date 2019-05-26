import pandas as pd
import xlrd
from scipy import stats

devfromfive = pd.read_excel('C:\Laba\lab_1.01.xlsx', sheet_name=0)
print(stats.kstest(devfromfive, 'norm', (devfromfive.mean(),devfromfive.std())))