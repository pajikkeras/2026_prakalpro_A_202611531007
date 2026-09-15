#Buat file dengan nama aritmatika_NIM.py
#Buat program untuk operator aritmatika dalam Python
#Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
#Program ini menggunakan fungsi input ()
#Nilai yang dimasukkan akan dikonversi menjadi tipe data integer

angka1_1007 = int(input("Input angka-1: "))
angka2_1007 = int(input("Input angka-2: "))

#Penjumalahan 
hasil_1007 = angka1_1007 + angka2_1007
print("\nOperator Penjumlahan")
print("Hasil =", hasil_1007)

#Pemgurangan
hasil_1007 = angka1_1007 - angka2_1007
print("\nOperator Pengurangan")
print("Hasil =", hasil_1007)

#Perkalian
hasil_1007 = angka1_1007 * angka2_1007
print("\nOperator Perkalian")
print("Hasil =", hasil_1007)

#Pembagian, pembagian bulat, dan sisa bagi
if angka2_1007 != 0:
    hasil_1007 = angka1_1007 / angka2_1007
    print("\nOperator Pembagian")
    print("Hasil =", hasil_1007)

    hasil_1007 = angka1_1007 // angka2_1007
    print("\nOperator Pembagian Bulat")
    print("Hasil =", hasil_1007)

    hasil = angka1_1007 % angka2_1007
    print("\nOperator Sisa Bagi")
    print("Hasil =", hasil_1007)
else:
    print("Angka kedua tidak bole bernilai 0.")

#Pangkat
hasil_1007 = angka1_1007 ** angka2_1007
print("\nOperator Pangkat")
print("Hasil =", hasil_1007)