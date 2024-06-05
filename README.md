# UAS-Pengkodean-D

**SOAL**

[1] Buatlah sebuah script Python yang membaca data penjualan dari file CSV.

[2] Lakukan pengelompokan data berdasarkan kategori produk dan hitung total penjualan (jumlah unit terjual dikalikan dengan harga per unit) untuk setiap kategori di setiap bulan.

[3] Visualisasikan total penjualan bulanan untuk setiap kategori produk menggunakan grafik garis.

[4] Tentukan kategori produk dengan total penjualan tertinggi selama periode Januari hingga November 2023.

[5] Lakukan analisis statistik sederhana untuk melihat tren penjualan per kategori produk. Hitung rata-rata dan standar deviasi penjualan bulanan untuk setiap kategori produk.

[6] Simpan hasil analisis statistik tersebut ke dalam file CSV baru.

![image](https://github.com/AdindaAurielSafira/TUGASUAS-ADINDAAURIELSAFIRA-AKUNTANSI-284/blob/main/Visualisasi-Total-Penjualan-per-Kategori-Produk.jpeg)

**ANALISIS TREN**

_Kain Jeans (Biru)_
Penjualan Kain Jeans cenderung lebih stabil dibandingkan kategori lainnya, dengan fluktuasi yang tidak terlalu tajam.
Terdapat kenaikan yang konsisten dari Januari hingga Mei, dan kemudian fluktuasi yang moderat setelahnya.

_Kain Sutra (Oranye)_
Penjualan Kain Sutra menunjukkan fluktuasi yang lebih tajam dibandingkan Kain Jeans.
Ada penurunan drastis pada bulan Februari, diikuti oleh kenaikan pada bulan Maret, dan fluktuasi yang signifikan pada bulan-bulan berikutnya.

_Kain Wol (Hijau)_
Kategori ini menunjukkan penjualan yang sangat fluktuatif.
Terdapat beberapa puncak tinggi, seperti pada bulan Maret dan Juni, tetapi juga beberapa penurunan tajam, menunjukkan penjualan yang tidak konsisten.

**Kesimpulan**
[1] Kain Wol memiliki penjualan tertinggi pada beberapa bulan tertentu (contohnya Maret dan Juni), tetapi juga memiliki penurunan yang tajam, menunjukkan adanya variabilitas yang tinggi.
[2] Kain Sutra menunjukkan fluktuasi yang signifikan, terutama di bulan-bulan awal, tetapi cenderung meningkat pada bulan terakhir (November).
[3] Kain Jeans cenderung lebih stabil, dengan kenaikan dan penurunan yang lebih moderat, menandakan penjualan yang lebih konsisten dibandingkan dua kategori lainnya.

![image](https://github.com/AdindaAurielSafira/TUGASUAS-ADINDAAURIELSAFIRA-AKUNTANSI-284/blob/main/Visualisasi-Analisis-Data.jpeg)

**ANALISIS DATA REGRESI SEDERHANA**

[1] Kain Jeans memiliki rata-rata penjualan bulanan yang lebih rendah dibandingkan Kain Wol tetapi lebih tinggi dari Kain Sutra.
[2] Kain Sutra memiliki rata-rata penjualan bulanan yang paling rendah di antara ketiga kategori produk.
[3] Kain Wol memiliki rata-rata penjualan bulanan tertinggi.

**Kesimpulan**
[1] Regresi linier sederhana digunakan untuk memahami apakah ada tren linier sederhana yang bisa menjelaskan variasi rata-rata penjualan bulanan berdasarkan kategori produk.
[2] Garis regresi menunjukkan tren peningkatan dari Kain Sutra ke Kain Wol. Namun, mengingat hanya ada tiga titik data (kategori produk), analisis ini sangat terbatas dan hasil regresi mungkin tidak sepenuhnya representatif.
[3] Jika ditujukan untuk analisis yang lebih mendalam, lebih banyak data atau kategori produk mungkin diperlukan untuk mengkonfirmasi hasil ini.

**Keterbatasan**
[1] Dengan hanya tiga kategori produk, regresi linier sederhana ini hanya menunjukkan tren dasar yang mungkin tidak cukup untuk membuat kesimpulan yang kuat.
[2] Interpretasi ini juga bergantung pada representasi numerik dari kategori produk, yang mungkin tidak mencerminkan variasi nyata dalam data produk.


