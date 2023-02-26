import pandas as pd
import matplotlib.pyplot as plt

# Lokasi file excel
path = ('/home/nuzia/VScode/BIG Project/Modul 2/PT.KOMPUTER .OK.xlsx')

# Mengambil data dari excel
df = pd.read_excel(path)

# Kalkulasi Rata-Rata berdasarkan Area Penjualan
means = df.groupby('Area')[
    ['Nilai Penjualan',
     'Masa Kerja',
     'Jumlah Toko']
].mean()

# Membuat grafik
# 'kind' bisa di ganti sesuai dengan penyajian data : 'barh','hist' dll
means.plot(kind='bar')

# Labelisasi x,y
plt.xlabel('Area Penjualan Sales')
plt.ylabel('Mean')

# Judul Grafik (Optional)
plt.title('Rata Rata Dari Nilai Penjualan,Masa Kerja,Jumlah Toko')

# Menampilkan Grafik
plt.show()