import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder

# Langkah 1: Membaca data dari file CSV
statistics = pd.read_csv('analisis_statistik_penjualan.csv')

# Langkah 2: Mengubah kategori produk menjadi nilai numerik
label_encoder = LabelEncoder()
statistics['Kategori Produk Numerik'] = label_encoder.fit_transform(statistics['Kategori Produk'])

# Langkah 3: Membuat model regresi linier sederhana
X = statistics[['Kategori Produk Numerik']]  # Fitur (kategori produk numerik)
y = statistics['mean']  # Target (rata-rata penjualan bulanan)

model = LinearRegression()
model.fit(X, y)

# Memprediksi nilai y berdasarkan model regresi
y_pred = model.predict(X)

# Langkah 4: Visualisasi hasil regresi
plt.figure(figsize=(10, 6))

# Menampilkan data asli
plt.scatter(statistics['Kategori Produk Numerik'], y, color='blue', label='Data Asli')

# Menampilkan garis regresi
plt.plot(statistics['Kategori Produk Numerik'], y_pred, color='red', linewidth=2, label='Garis Regresi')

# Menambahkan label dan judul
plt.xlabel('Kategori Produk (Numerik)')
plt.ylabel('Rata-rata Penjualan Bulanan')
plt.title('Regresi Linier Sederhana: Kategori Produk vs Rata-rata Penjualan Bulanan')
plt.xticks(statistics['Kategori Produk Numerik'], statistics['Kategori Produk'], rotation=45)
plt.legend()

# Menampilkan plot
plt.show()
