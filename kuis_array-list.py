"""
TODO:
Sebuah variabel array diberikan dengan ketentuan berikut.
- Variabel array bernama "var_array" dengan nilai dari 0 hingga 100.
- Hitung nilai rata-rata dari elemen array tersebut.
- Simpan hasil perhitungan dalam variabel bernama "result".

Tips:
- Rumus menghitung rata-rata adalah jumlah seluruh elemen dibagi banyaknya elemen.
- Gunakan percabangan dan perulangan untuk mempermudah,
  Anda tidak diperbolehkan memberikan nilai secara langsung.
"""
# Jangan ubah kode ini
var_array = [i for i in range(101)]

# TODO: Silakan buat kode Anda di bawah ini.

# Inisialisasi variabel untuk jumlah elemen dan total nilai elemen
total_sum = 0
num_elements = 0

# Menggunakan perulangan untuk menghitung total nilai dan jumlah elemen
for value in var_array:
    total_sum += value
    num_elements += 1

# Menghitung rata-rata
result = total_sum / num_elements

# Menampilkan hasil
print("Nilai rata-rata:", result)
