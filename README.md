# 💻 Klasifikasi Kelayakan Kredit Komputer

Proyek ini bertujuan untuk membangun model klasifikasi menggunakan algoritma **Naive Bayes** untuk menentukan apakah seseorang layak mendapatkan kredit komputer berdasarkan data dummy yang telah disediakan.

---

## 📁 Dataset

Dataset dapat diunduh melalui link berikut:  
🔗 [Download Dataset](https://drive.google.com/file/d/1krLRWedghy_ysJ2N6i-1GJ-ZQUmnu6eu/view?usp=sharing)

Dataset ini berisi data dummy pengajuan kredit komputer dengan berbagai fitur seperti penghasilan, status pekerjaan, status pernikahan, dan lain-lain.

---

## 🧠 Algoritma yang Digunakan

- **Naive Bayes Classifier** (Gaussian Naive Bayes)

---

## ⚙️ Tahapan Pembuatan Model

### 1. Import Library
Import pustaka yang diperlukan seperti `pandas`, `sklearn`, `numpy`, dll.

### 2. Load Dataset
Membaca file CSV yang berisi data dummy kredit komputer.

### 3. Exploratory Data Analysis (EDA)
- Menampilkan informasi umum dari dataset
- Cek missing value
- Cek distribusi data

### 4. Preprocessing Data
- Menangani missing value (jika ada)
- Encoding fitur kategorikal menggunakan LabelEncoder
- Memisahkan fitur (X) dan target (y)

### 5. Split Data
Membagi dataset menjadi data training dan testing (contoh: 80% train, 20% test)

### 6. Training Model
Melatih model menggunakan Gaussian Naive Bayes.

### 7. Evaluasi Model
Melakukan evaluasi model menggunakan metrik:
- Akurasi
- Confusion Matrix
- Classification Report (precision, recall, f1-score)

---

## 📊 Hasil Evaluasi

```text
Akurasi: 0.74

Confusion Matrix:
 [[ 28  43]
 [  9 120]]

Classification Report:
               precision    recall  f1-score   support

           0       0.76      0.39      0.52        71
           1       0.74      0.93      0.82       129

    accuracy                           0.74       200
   macro avg       0.75      0.66      0.67       200
weighted avg       0.74      0.74      0.71       200

Analisis Hasil:
- Akurasi model sebesar 74% menunjukkan bahwa model cukup baik dalam mengklasifikasikan data.
- Kelas 1 (layak kredit) memiliki recall tinggi (93%), artinya model berhasil mengenali sebagian besar individu yang memang layak kredit.
- Namun, kelas 0 (tidak layak) memiliki recall rendah (39%), artinya banyak orang yang tidak layak malah diprediksi layak oleh model (false positive tinggi).
- Hal tersebut menunjukkan adanya ketidakseimbangan prediksi dan model cenderung bias terhadap kelas mayoritas (layak kredit).