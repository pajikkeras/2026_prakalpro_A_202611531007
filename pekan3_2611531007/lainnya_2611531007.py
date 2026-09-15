# Buat file dengan nama lainnya_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input ()
# Program operator keanggotaan dan identitas

print("================================")
print("1. OPERATOR KEANGGOTAAN")
print("================================")

# Input beberapa data yang dipisahkan dengan koma
input_data_1007 = input("Masukkan beberapa angka, pisahkan dengan koma: ")

# Mengubah input menjadi list integer
data_1007 = [int(angka.strip()) for angka in input_data_1007.split(",")]

nilai_dicari_1007 = int(input("Masukkan angka yang ingin dicari: "))

# Operator in
hasil_1007 = nilai_dicari_1007 in data_1007
print("\nOperator keanggotan IN")
print(nilai_dicari_1007, "in", data_1007, "=", hasil_1007)

# Operator not in
hasil_1007 = nilai_dicari_1007 not in data_1007
print("\nOperator Keanggotaan NOT IN")
print(nilai_dicari_1007, "not in", data_1007, "=", hasil_1007)

print("\n========================")
print("2. OPERATOR IDENTITAS")
print("========================")

# objek menggunakan list dari input pengguna
objek1_1007 = data_1007

# objek merujuk pada objek yang sama dengan objek1_1007
objek2_1007 = objek1_1007

# objek memiliki isi sama, tetapi merupakan objek baru
objek3_1007 = data_1007.copy()

print("objek1_1007 =", objek1_1007)
print("objek2_1007 =", objek2_1007)
print("objek3_1007 =", objek3_1007)

# Operator is
hasil_1007 = objek1_1007 is objek2_1007
print("\nOperator Identitas IS")
print("objek1_1007 is objek2_1007 =", hasil_1007)

# Operator is not
hasil_1007 = objek1_1007 is not objek3_1007
print("\nOperator Identitas IS NOT")
print("objek1_1007 is not objek3_1007 =", hasil_1007)

# Membandingkan identitas dan nilai
print("\nPerbandingan identitsa dan nilai")
print("obejk1_1007 is objek3_1007 =", objek1_1007 is objek3_1007)
print("objek1_1007 == obje3_1007 =", objek1_1007 == objek3_1007)
