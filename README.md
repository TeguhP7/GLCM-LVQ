Program Deteksi Masker Menggunakan Metode Gray Level Co-Occurrence Matrix Berdasarkan Klasifikasi Learning Vector Quantization:

Program deteksi masker menggunakan metode Gray Level Co-Occurrence Matrix (GLCM) berdasarkan klasifikasi Learning Vector Quantization (LVQ) adalah sebuah aplikasi berbasis komputer yang dirancang untuk mengidentifikasi apakah seseorang sedang memakai masker wajah atau tidak. Program ini menggabungkan teknik pengolahan citra dengan kecerdasan buatan untuk melakukan analisis terhadap citra wajah manusia dan memprediksi adanya pemakaian masker atau tidak.

Metode GLCM digunakan dalam program ini untuk mengekstraksi informasi tekstur (fitur/ciri) dari citra wajah. GLCM adalah suatu representasi statistik yang menggambarkan hubungan spasial antara pasangan piksel dalam citra. Informasi ini dapat memberikan wawasan tentang distribusi intensitas piksel dalam citra dan membantu mengidentifikasi pola tekstur yang khas, seperti tekstur kulit wajah dengan atau tanpa masker.

Selanjutnya, untuk mengklasifikasikan apakah seseorang menggunakan masker atau tidak, program ini menggunakan algoritma Learning Vector Quantization (LVQ). LVQ adalah metode pembelajaran yang memetakan data masukan ke dalam kelas-kelas tertentu berdasarkan vektor-vektor pembelajaran. Dalam konteks ini, vektor-vektor pembelajaran akan mencerminkan karakteristik tekstur yang terkait dengan citra wajah yang memakai  dan yang tidak memakai masker.

Proses kerja program ini dapat dijelaskan sebagai berikut:

1. **Pengumpulan Data**: Program akan mengambil citra wajah sebagai data masukan. Data ini bisa berupa citra yang diambil secara real-time menggunakan kamera atau diimpor dari sumber lain. Dalam program kali ini saya menggunakan beberapa dataset wajah yang memakai dan tidak memakai masker yang berasal dari  Dataset Kaggle (https://www.kaggle.com/) 

2. **Ekstraksi Fitur dengan GLCM**: Setelah mendapatkan citra wajah, program akan menghitung matriks GLCM dari citra tersebut. Informasi tekstur yang dihasilkan dari GLCM akan dijadikan fitur yang akan digunakan dalam proses klasifikasi. GLCM memiliki tiga parameter utama, yaitu arah sudut (0, 45, 90, 135), jarak piksel yang berdekatan, dan tingkat keabuan piksel (gray tone). Terdapat 6 fitur yang akan kita gunakan dalam program ini yaitu contrast, dissimilarity, homogeneity, angular second moment (ASM), energy, and correlation.

3. **Pelatihan Model LVQ**: Model LVQ akan dilatih menggunakan sejumlah data latih (training data) yang sudah diberi label yaitu 'Memakai' dan 'Tidak Memakai' masker. Data latih yang diolah LVQ berupa fitur-fitur yang telah didapat dari metode ekstrasi GLCM sebelumnya.

4. **Klasifikasi**: Setelah model LVQ terlatih, program akan menggunakan model ini untuk mengklasifikasikan citra wajah baru berdasarkan fitur-fitur GLCM yang dihasilkan. Hasil klasifikasi ini akan menentukan apakah citra tersebut menggambarkan seseorang yang memakai atau tidak memakai masker.

5. **Tampilan Hasil**: Program akan menampilkan hasil klasifikasi kepada pengguna pada tampilan aplikasi yang bertuliskan Memakai atau Tidak Memakai masker.

Program ini mampu untuk mendeteksi penggunaan masker dengan memanfaatkan informasi tekstur dalam citra waja. Namun, program ini juga memerlukan dataset latih yang berkualitas dan cakupan variasi kondisi yang luas agar mampu menghasilkan model klasifikasi yang handal.

Berdasarkan hasil pelatihan dan pengujian program masih dapat dikembangkan dengan menggunakan metode ekstraksi dan/atau metode klasifikasi lainnya.
