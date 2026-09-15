# Buat file dengan nama perbandingan_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input ()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer
# Program operator perbandingan dalam Python

angka1_1007 = int(input("Input Angka-1: "))
angka2_1007 = int(input("Input Angka-2: "))

# Lebih besar dari
hasil_1007 = angka1_1007 > angka2_1007
print("\nOperator lebih besar dari")
print("angka1_1007 > angka2_1007 =", hasil_1007)

# Lebih kecil dari
hasil_1007 = angka1_1007 < angka2_1007 
print("\nOperator lebih kecil dari")
print("angka1_1007 < angka2_1007 =", hasil_1007)

# Lebih besar dari atau sama dengan
hasil_1007 = angka1_1007 >= angka2_1007
print("\nOperator lebih besar dari atau sama dengan")
print("angka1_1007 >= angka2_1007 =", hasil_1007)

# Lebih kecil dari atau sama dengan
hasil_1007 = angka1_1007 <= angka2_1007
print("\nOperator Lebih kecil dari atau sama dengan")
print("angka1_1007 <= angka2_1007 =", hasil_1007)

# Sama dengan
hasil_1007 = angka1_1007 == angka2_1007
print("\nOperator sama dengan")
print("angka1_1007 == angka2_1007 =", hasil_1007)

# Tidak sama dengan
hasil_1007 = angka1_1007 != angka2_1007
print("\nOperator tidak saam dengan")
print("angka1_1007 != angka2_1007 =", hasil_1007)

# Tambahan perbandingan berantai dalam python
hasil_1007 = 0 < angka1_1007 < 100
print("\nPerbandingan berantai")
print("0 < angka1_1007 <100 =", hasil_1007)

hasil_1007 = 0 < angka2_1007 < 100
print("0 < angka2_1007 < 100 =", hasil_1007)