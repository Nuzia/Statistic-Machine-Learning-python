import pandas as pd
import scipy.stats as stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# Lokasi file excel
path = ('/home/nuzia/VScode/FKOM Bangkit/Modul 2/PT.KOMPUTER .OK.xlsx')

# Mengambil data dari excel
df = pd.read_excel(path)

# One-way ANOVA
anova_model = ols(
    'NilaiPenjualan ~ C(Pendidikan)',
    data=df).fit()

anova_table = sm.stats.anova_lm(anova_model, typ=2)

tukey_results = pairwise_tukeyhsd(
    df['NilaiPenjualan'],
    df['Pendidikan']
    .astype('category'),
    alpha=0.05)

# menampilkan hasil
print("One way Anova :")
print(anova_table)
print(tukey_results)
