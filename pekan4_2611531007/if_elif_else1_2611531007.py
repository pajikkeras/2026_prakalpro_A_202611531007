# Buat file dengan nama if_elif_else1_NIM.py
# Buat program untuk kondisional if 
# Nama variabel ditambah 4 digit nim terakhir, contoh: ipk_1234
# Program ini menggunakan fungsi input ()

umur_1007 = int(input("Input umur anda: "))
sim_1007 = input(input("Apakah Anda Sudah Punya Sim C (y/t)")) [0]

if umur_1007 >= 117 and sim_1007 == 'y': 
    print("Anda Sudag deawsa dan bole bawa motor")

elif umur_1007 >= 17 and sim_1007 != 'y':
    print("Anda Sudah deawasa tetapi tidak boleh membawa motor")

elif umur_1007 < 17 and sim_1007 == 'y':
    print("Anda Belum Cukup Umur punya SIM")

else :
    print("Anda Belum Cukup Umur bawa motor")

print("Program Selesai")  
