import pandas as pd
import plotly.express as px

# Lokasi file excel
path = ('/home/nuzia/VScode/BIG Project/Modul 2/PT.KOMPUTER .OK.xlsx')

# Mengambil data dari excel
df = pd.read_excel(path)

# create bar chart using Plotly
fig = px.bar(df, x='Jumlah Toko', title='Sales by Category')

# show plot
fig.show()