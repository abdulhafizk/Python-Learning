"""
TODO:
Buatlah sebuah fungsi bernama "minimal" dengan ketentuan berikut.
- Menerima dua buah argumen berupa number, yaitu a dan b.
- Mengembalikan nilai terkecil antara a atau b.
- Bila nilai keduanya sama, kembalikan dengan nilai a.
"""


# TODO: Silakan buat kode Anda di bawah ini.

def minimal(a, b):
    # Mengembalikan nilai terkecil antara a dan b
    # Jika nilai keduanya sama, mengembalikan nilai a
    return min(a, b)

# Contoh penggunaan fungsi
a = 5
b = 10
print("Nilai minimal antara", a, "dan", b, "adalah", minimal(a, b))
