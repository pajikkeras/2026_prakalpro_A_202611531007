# Buat file dengan nama if2_NIM.py
# Buat program untuk kondisional if 
# Nama variabel ditambah 4 digit nim terakhir, contoh: ipk_1234
# Program ini menggunakan fungsi input ()

ipk_1007 = float(input("Input IPK Anda = "))

if ipk_1007 > 2.75:
    print("Anda Lulus Sangat Memuaskan dengan IPK " + str (ipk_1007))
else:
    print("Anda Tidak Lulus")

print("Prgram Selesai")