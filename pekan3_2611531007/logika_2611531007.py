# Buat file dengan nama logika_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: a1_1234
# Program ini menggunakan fungsi input ()
# Program operator logika dalam Python

# Memasukkan nilai boolean
# Input tidak peka terhdap huruf besar dan kecil
a1_1007 = input("Input nilai Boolean-1 (true/false): ").strip().lower() == "true"
a2_1007 = input("Input nilai Boolean-1 (true/false): ").strip().lower() == "true"

print("\nA1_1007 =", a1_1007)
print("A2_1007 =", a2_1007)

# Konjungsi: bernilai True dika keduanya True
hasil_1007 = a1_1007 and a2_1007
print("\nKonjungsi (AND)")
print("A1 and A2 =", hasil_1007)

# Disjungsi: bernilai True jika salah satunya True
hasil_1007 = a1_1007 or a2_1007
print("\nDisjungsi (OR)")
print("A1_1007 or A2_1007 =", hasil_1007)

# Negasi A2: membalik nilai A2
hasil_1007 = not a2_1007
print("\nNegasi A2_1007 (NOT)")
print("not A2_1007 =", hasil_1007)

# XOR: bernilai True jika kedua nilai berbeda
hasil_1007 = a1_1007 != a2_1007
print("\nDisjungsi Eksklusif (XOR)")
print("A1_1007 XOR A2_1007 =", hasil_1007)


