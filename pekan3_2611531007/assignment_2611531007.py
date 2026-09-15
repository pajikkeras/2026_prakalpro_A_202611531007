# Buat file dengan nama assignment_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input ()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer
# Program operator assignmet dalam python

angka1_1007 = int(input("Input angka-1: "))
angka2_1007 = int(input("Input angka-2: "))

print("\nNilai awal angka1_1007 =", angka1_1007)
print("Nilai angka2_1007 =", angka1_1007)

# Assignment penambahan
hasil_1007 = angka1_1007
hasil_1007 += angka2_1007
print("\nAssignment penambahan (+=)")
print("Hasil =", hasil_1007)

# Assignment pengurangan
hasil_1007 = angka1_1007
hasil_1007 -= angka2_1007
print("\nAssignment penguranngan (-=)")
print(("Hasil =", hasil_1007))

# Assignment perkalian 
hasil_1007 = angka1_1007
hasil_1007 *= angka2_1007
print("\nAssignment perkalian (*=)")
print("Hasil =", hasil_1007)

# Assignmnet pembagian, pembagian bulat, dan sisa bagi
if angka2_1007 != 0:
    hasil_1007 = angka1_1007
    hasil_1007 /= angka2_1007
    print("\nAssignment pembagian bulat (/=)")
    print("Hasil =", hasil_1007)
    
    #Operator tambahan
    hasil_1007 = angka1_1007
    hasil_1007 //= angka2_1007
    print("\nAssignment pembagian bulau (//=)")
    print("Hasil =", hasil_1007)
    hasil_1007 = angka1_1007
    hasil_1007 %= angka2_1007
    print("\nAssignment sisa bagi (%=)")
    print("Hasil =", hasil_1007)
else:
    print("\nPembagian tidak dapat dilakukan")
    print("Angka kedau tidak bole bernilai 0")

# Operator tambahan assignment perpangkatan
hasil = angka1_1007
hasil_1007 **= angka2_1007
print("\nAssignment perpangkatan (**=)")
print("Hasil =", hasil_1007)
