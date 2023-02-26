import pandas as pd
from scipy.stats import f_oneway

# Lokasi file excel
path = ('/home/nuzia/VScode/FKOM Bangkit/Modul 2/PT.KOMPUTER .OK.xlsx')

# Mengambil data dari excel
df = pd.read_excel(path)

sma_sales = df.loc[df['Pendidikan'] == 'SMA', 'NilaiPenjualan']
d3_sales = df.loc[df['Pendidikan'] == 'D3', 'NilaiPenjualan']
s1_sales = df.loc[df['Pendidikan'] == 'S1', 'NilaiPenjualan']

# Perform one-way ANOVA
f_stat, p_val = f_oneway(sma_sales, d3_sales, s1_sales)

# Print results
print('One-way ANOVA results:')
print('F-statistic:', f_stat)
print('p-value:', p_val)
