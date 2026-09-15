# Buat file dengan nama bitwise_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()

print("================================")
print("3. OPERATOR BITWISE")
print("================================")

angka1_1007 = int(input("Masukkan angka bitwise-1: "))
angka2_1007 = int(input("Masukkan angka bitwise-2: "))

print("\nAngka dalam bentuk desimal dan biner")
print("angka1_1007 =", angka1_1007, "| biner =", bin(angka1_1007))
print("angka2_1007 =", angka2_1007, "| biner =", bin(angka2_1007))

# Bitwise AND
hasil_1007 = angka1_1007 & angka2_1007
print("\nBitwise AND (&)")
print(angka1_1007, "&", angka2_1007)
print("Biner hasik (8 bit) =", format(hasil_1007, "08b"))

# Bitwise OR
hasil_1007 = angka1_1007 |angka2_1007
print("\nBitwise OR (|)")
print(angka1_1007, "|", angka2_1007, "=", hasil_1007)
print("Biner hasil =", bin(hasil_1007))
print("Biner hasil (8 bit) =", format(hasil_1007, "08b"))

# Bitwise XOR
hasil_1007 = angka1_1007 ^ angka1_1007
print("\nBitwise XOR (^)")
print(angka1_1007)
