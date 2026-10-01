print("=== PROGRAM JAM PASIR KRISTAL PALINDROMIK (PEKAN 5) ===")
n_1007 = int(input("Masukkan ukuran skala jam pasir (N): "))

print("#", end="")
for pagar_1007 in range(4 * n_1007 + 5):
    print("=", end="")
print("#")

for baris_1007 in range(n_1007, 0, -1):
    print("| ", end="")
    for spasi_kiri_1007 in range(2 * (n_1007 - baris_1007)):
        print(" ", end="")
    for angka_1007 in range(baris_1007, 0, -1):
        print(angka_1007, end=" ")
    print("<*>", end="")
    for angka_1007 in range(1, baris_1007 + 1):
        print(" " + str(angka_1007), end="")
    for spasi_kanan_1007 in range(2 * (n_1007 - baris_1007)):
        print(" ", end="")
    print(" |")

print("|", end="")
for spasi_kiri_1007 in range(2 * n_1007 + 1):
    print(" ", end="")
print("<*>", end="")
for spasi_kanan_1007 in range(2 * n_1007 + 1):
    print(" ", end="")
print("|")

for baris_1007 in range(1, n_1007 + 1):
    print("| ", end="")
    for spasi_kiri_1007 in range(2 * (n_1007 - baris_1007)):
        print(" ", end="")
    for angka_1007 in range(baris_1007, 0, -1):
        print(angka_1007, end=" ")
    print("<*>", end="")
    for angka_1007 in range(1, baris_1007 + 1):
        print(" " + str(angka_1007), end="")
    for spasi_kanan_1007 in range(2 * (n_1007 - baris_1007)):
        print(" ", end="")
    print(" |")

print("#", end="")
for pagar_1007 in range(4 * n_1007 + 5):
    print("=", end="")
print("#")

