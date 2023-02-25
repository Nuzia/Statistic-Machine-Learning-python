import pandas as pd
import matplotlib.pyplot as plt

#Lokasi file excel
path = ('/home/nuzia/VScode/BIG Project/Modul 2/PT.KOMPUTER .OK.xlsx')

#mengambil data dari excel
data = pd.read_excel(path)

# Memuat DataFrame dari data
df = pd.DataFrame(data)

# Membuat bar
plt.bar(
    df['Area'],
    df['Nilai Penjualan'],
)

# setting kordinat x,y 
plt.xlabel('Area Penjualan Sales')
plt.ylabel('Nilai Penjualan (Juta Rupiah)')

# menampilkan grafik
plt.show()