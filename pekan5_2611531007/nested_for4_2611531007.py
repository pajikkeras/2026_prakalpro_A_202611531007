# Buat file dengan nama nested_for4_NIM.py
# Buat program untuk perulangan for dalam Python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

tinggi_1007 = int(input("Masukkan tinggi pola (bilangan genap, misal 10): "))

if tinggi_1007 % 2 != 0:
    print("Tinggi harus bilangan genap!")
else:
    a_1007 = tinggi_1007
    c_1007 = a_1007
    lebar_1007 = (2 * tinggi_1007) - 2

    for i_1007 in range(1, tinggi_1007 + 1):
        b_1007 = c_1007 + 1
        
        for j_1007 in range(1, lebar_1007 + 1):
            
            # Baris atas dan bawah
            if i_1007 == 1 or i_1007 == tinggi_1007:
                if j_1007 == 1 or j_1007 == lebar_1007:
                    print("#", end="")
                else:
                    print("=", end="")
            # Baris isi
            else:
                if j_1007 == 1 or j_1007 == lebar_1007:
                    print("|", end="")
                else:
                    if j_1007 == c_1007:
                        print("<", end="")
                    elif j_1007 == b_1007:
                        print(">", end="")
                    elif j_1007 == (lebar_1007 - c_1007):
                        print("<", end="")
                    elif j_1007 == (lebar_1007 - c_1007 + 1):
                        print(">", end="")
                    elif j_1007 > b_1007 and j_1007 < (lebar_1007 - c_1007):
                        print(".", end="")
                    else:
                        print(" ", end="")

        print()

        # Logika asli Java
        a_1007 -= 2

        if a_1007 <= 0:
            c_1007 = (-a_1007) + 2
        else:
            c_1007 = a_1007