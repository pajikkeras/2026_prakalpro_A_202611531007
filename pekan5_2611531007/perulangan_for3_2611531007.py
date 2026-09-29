# Buat file dengan nama perulangan_for3_NIM.py
# Buat program untuk perulangan for dalam Python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

ulang_1007 = int(input("Masukkan jumlah perulangan: "))

jumlah = 0
for i in range(1, ulang_1007 + 1):
    print(i, end=" ")
    jumlah = jumlah + i
    
    if i < ulang_1007:
        print(" + ", end="")
    else:
        print(" = ", jumlah, end="")
print()
print("Jumlah =", jumlah)