import pandas as pd
import matplotlib.pyplot as plt

# Lokasi file excel
path = ('/home/nuzia/VScode/BIG Project/Modul 2/PT.KOMPUTER .OK.xlsx')

# Mengambil data dari excel
df = pd.read_excel(path)

df.plot(x='Area', y='Nilai Penjualan',kind='bar')
plt.show()