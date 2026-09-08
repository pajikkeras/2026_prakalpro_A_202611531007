# Buat file dengan nama Konstanta_1234
# Programini menggunakan konstanta untuk menghitung luas lingkaran
# nama variabel ditambah 4 digit nim terakhir contoh: jari_1234

from typing import Final
PI: Final = 3.14
print("pi: %F" % (PI))
jari_1007 = float(input('Masukkan nilai jari jari: '))
luas_1007 = PI * jari_1007 * jari_1007
print("Luas Lingkaran dengan jari-jari %.2f adalah %.2f" % (jari_1007, luas_1007))