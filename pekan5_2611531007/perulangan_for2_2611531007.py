# Buat file dengan nama perulangan_for2_NIM.py
# Buat program untuk perulangan for dalam Python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

ulang_1007 = int(input ("Masukkan jumlah perulangan:"))
print("Perulangan ke-0 sampai ke-", ulang_1007-1)

for i in range(ulang_1007):
    print(i, end=" ")
print()
print("Perulangan ke-1 sampai ke-", ulang_1007)
for i in range(ulang_1007):
    print(i+1, end=" ")