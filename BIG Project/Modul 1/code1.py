import pandas as pd

# memasukan data
data = [
    ['a', 'Laki Laki', 'Petani', 2, 1.2],
    ['b', 'Perempuan', 'Buruh', 1, 1.3],
    ['c', 'Laki Laki', 'Pedagang', 1, 1.4],
    ['d', 'Perempuan', 'Pedagang', 6, 1]
]

# membuat header tabel dari dataframe
df = pd.DataFrame(data, columns=['nama', 'gender', 'jenis pekerjaan', 'jumlah tanggungan' , 'jumlah penghasilan'])

# print the DataFrame
print(df)