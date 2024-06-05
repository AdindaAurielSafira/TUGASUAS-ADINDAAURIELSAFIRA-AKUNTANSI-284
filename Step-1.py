import pandas as pd

# Membaca data dari file CSV
data = pd.read_csv('Penjualan.csv', delimiter=';')
print(data.head())

# Menambahkan kolom Total Penjualan
data['Total Penjualan'] = data['Jumlah Unit Terjual'] * data['Harga per Unit']

# Mengubah kolom 'Tanggal' menjadi tipe datetime
data['Tanggal'] = pd.to_datetime(data['Tanggal'], format='%d/%m/%Y')

# Menambahkan kolom Bulan
data['Bulan'] = data['Tanggal'].dt.to_period('M')

# Mengelompokkan data berdasarkan Kategori Produk dan Bulan, lalu menghitung total penjualan
grouped_data = data.groupby(['Kategori Produk', 'Bulan']).agg({'Total Penjualan': 'sum'}).reset_index()
print(grouped_data.head())

import matplotlib.pyplot as plt

# Membuat grafik garis total penjualan bulanan per kategori produk
plt.figure(figsize=(14, 8))
for category in grouped_data['Kategori Produk'].unique():
    category_data = grouped_data[grouped_data['Kategori Produk'] == category]
    plt.plot(category_data['Bulan'].astype(str), category_data['Total Penjualan'], label=category)

plt.xlabel('Bulan')
plt.ylabel('Total Penjualan')
plt.title('Total Penjualan Bulanan per Kategori Produk')
plt.legend()
plt.xticks(rotation=45)
plt.show()

# Menghitung total penjualan untuk setiap kategori produk selama periode Januari hingga November 2023
total_sales_per_category = grouped_data.groupby('Kategori Produk')['Total Penjualan'].sum()

# Menentukan kategori produk dengan total penjualan tertinggi
highest_sales_category = total_sales_per_category.idxmax()
print(f'Kategori produk dengan total penjualan tertinggi: {highest_sales_category}')

# Menghitung rata-rata dan standar deviasi penjualan bulanan untuk setiap kategori produk
statistics = grouped_data.groupby('Kategori Produk')['Total Penjualan'].agg(['mean', 'std']).reset_index()
print(statistics)

# Menyimpan hasil analisis statistik ke dalam file CSV baru
statistics.to_csv('analisis_statistik_penjualan.csv', index=False)
print('Hasil analisis statistik disimpan ke dalam file analisis_statistik_penjualan.csv')
