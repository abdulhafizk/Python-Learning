"""
TODO:
1. Buatlah class bernama Animal dengan ketentuan:
    - Memiliki properti:
      - name: string
      - age: int
      - species: string
    - Memiliki constructor untuk menginisialisasi properti:
      - name
      - age
      - species
2. Buatlah class bernama Cat dengan ketentuan:
    - Merupakan turunan dari class Animal
    - Memiliki method:
      - bernama "deskripsi" yang mengembalikan nilai string berikut ini.
        "{self.name} adalah kucing berjenis {self.species} yang sudah berumur {self.age} tahun"
      - bernama "suara" yang akan mengembalikan nilai string "meow!"
 3. Buatlah instance dari kelas Cat bernama "myCat" dengan ketentuan:
    - Atribut name bernilai: "Neko"
    - Atribut age bernilai: 3
    - Atribut species bernilai: "Persian".
"""

#TODO: Silakan buat kode Anda di bawah ini.


class Animal:
  """
  Kelas untuk mendefinisikan hewan.

  Properti:
    - name: Nama hewan (string)
    - age: Usia hewan (int)
    - species: Jenis hewan (string)

  Metode:
    - __init__(self, name, age, species): Constructor untuk menginisialisasi properti.
  """

  def __init__(self, name, age, species):
    self.name = name
    self.age = age
    self.species = species

class Cat(Animal):
  """
  Kelas untuk mendefinisikan kucing.

  Warisan:
    - Animal: Kelas dasar hewan.

  Metode:
    - deskripsi(self): Mengembalikan deskripsi kucing.
    - suara(self): Mengembalikan suara kucing.
  """

  def deskripsi(self):
    """
    Mengembalikan deskripsi kucing.

    Contoh:
      "Neko adalah kucing berjenis Persian yang sudah berumur 3 tahun"
    """
    return f"{self.name} adalah kucing berjenis {self.species} yang sudah berumur {self.age} tahun"

  def suara(self):
    """
    Mengembalikan suara kucing.

    Contoh:
      "meow!"
    """
    return "meow!"

# Buat instance dari kelas Cat
myCat = Cat(name="Neko", age=3, species="Persian")

# Cetak deskripsi dan suara kucing
print(myCat.deskripsi())
print(myCat.suara())
