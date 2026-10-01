# Buat file dengan nama perulangan_for2_NIM.py
# Buat program untuk perulangan for dalam Python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

ulang_1007 = int(input ("Masukkan jumlah perulangan:"))
print("Perulangan ke-0 sampai ke-", ulang_1007-1)

for i_1007 in range(ulang_1007):
    print(i_1007, end=" ")
print()
print("Perulangan ke-1 sampai ke-", ulang_1007)
for i_1007 in range(ulang_1007):
    print(i_1007+1, end=" ")