<<<<<<< HEAD
# Buat file dengan nama nested_for1_NIM.py
# Buat program untuk perulangan for dalam Python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

batas_1007 = int(input("Masukkan nilai batas: "))
for line in range(1, batas_1007 + 1):
    for j in range(1, (-1 * line + batas_1007) + 1):
        print(".", end="")
=======
# Buat file dengan nama nested_for1_NIM.py
# Buat program untuk perulangan for dalam Python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

batas_1007 = int(input("Masukkan nilai batas: "))
for line in range(1, batas_1007 + 1):
    for j in range(1, (-1 * line + batas_1007) + 1):
        print(".", end="")
>>>>>>> c52c8860a95669d159a5db819e6ab4dcd5371ffd
    print(line)