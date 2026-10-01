# Buat file dengan nama perulangan_for3_NIM.py
# Buat program untuk perulangan for dalam Python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

ulang_1007 = int(input("Masukkan jumlah perulangan: "))

jumlah_1007 = 0
for i_1007 in range(1, ulang_1007 + 1):
    print(i_1007, end=" ")
    jumlah_1007 = jumlah_1007 + i_1007
    
    if i_1007 < ulang_1007:
        print(" + ", end="")
    else:
        print(" = ", jumlah_1007, end="")
print()
print("Jumlah =", jumlah_1007)