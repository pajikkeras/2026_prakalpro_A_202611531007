print("===== SISTEM TRANSAKSI TOKO =====\n")

# 1. INPUT DATA PELANGGAN DAN TRANSAKSI
nama_1007 = input("Masukkan Nama Pelanggan : ")
status_1007 = input("Masukkan Status Pelanggan (member/nonmember) : ")
total_1007 = float(input("Masukkan Total Belanja : "))
jumlah_1007 = int(input("Masukkan Jumlah Barang : "))
promo_1007 = input("Masukkan Kode Promo : ")

print("\n===== DATA TRANSAKSI =====")
print(f"Nama Pelanggan       : {nama_1007}")
print(f"Status Pelanggan     : {status_1007}")
print(f"Total Belanja        : Rp{total_1007:}")
print(f"Jumlah Barang        : {jumlah_1007}")
print(f"Kode Promo           : {promo_1007}")

# Daftar kode promo yang tersedia di toko
daftar_promo_1007 = ["HEMAT10", "HEMAT20", "GRATISONGKIR"]

# 2. OPERATOR PERBANDINGAN
syarat_belanja_1007 = total_1007 >= 200000          
syarat_barang_1007 = jumlah_1007 >= 3                
is_member_1007 = status_1007 == "member"             

# 3. OPERATOR KEANGGOTAAN (in / not in)
promo_tersedia_1007 = promo_1007 in daftar_promo_1007
promo_tidak_tersedia_1007 = promo_1007 not in daftar_promo_1007


# 4. OPERATOR LOGIKA (and, or, not)
diskon_member_1007 = is_member_1007 and syarat_belanja_1007
dapat_promo_1007 = promo_tersedia_1007 and (syarat_belanja_1007 or syarat_barang_1007)
bukan_member_1007 = not is_member_1007

print("\n===== HASIL VALIDASI =====")
print(f"Belanja >= Rp200000        : {syarat_belanja_1007}")
print(f"Jumlah Barang >= 3         : {syarat_barang_1007}")
print(f"Status Member              : {is_member_1007}")
print(f"Kode Promo Tersedia        : {promo_tersedia_1007}")
print(f"Mendapatkan Diskon Member  : {diskon_member_1007}")
print(f"Mendapatkan Promo          : {dapat_promo_1007}")

# 5. OPERATOR ARITMATIKA
diskon_persen_1007 = 0.10 if diskon_member_1007 else 0.0
besar_diskon_1007 = total_1007 * diskon_persen_1007
total_bayar_1007 = total_1007 - besar_diskon_1007
rata_rata_1007 = total_bayar_1007 / jumlah_1007

# 6. OPERATOR PENUGASAN (termasuk augmented assignment)
akumulasi_bayar_1007 = 0
akumulasi_bayar_1007 += total_bayar_1007
akumulasi_bayar_1007 *= 1

print("\n===== HASIL PERHITUNGAN =====")
print(f"Diskon                     : Rp{besar_diskon_1007:.0f}")
print(f"Total Pembayaran           : Rp{total_bayar_1007:.0f}")
print(f"Rata-rata Harga Barang     : Rp{rata_rata_1007:.0f}")

# 7. OPERATOR IDENTITAS (is / is not)
obj_a_1007 = daftar_promo_1007
obj_b_1007 = daftar_promo_1007
obj_c_1007 = ["HEMAT10", "HEMAT20", "GRATISONGKIR"]

identitas_sama_1007 = obj_a_1007 is obj_b_1007
identitas_beda_1007 = obj_a_1007 is not obj_c_1007
nilai_sama_1007 = obj_a_1007 == obj_c_1007

# 8. OPERATOR BITWISE - Kode Status Transaksi
bit_member_1007 = 0b0001 if is_member_1007 else 0b0000
bit_belanja_1007 = 0b0010 if syarat_belanja_1007 else 0b0000
bit_barang_1007 = 0b0100 if syarat_barang_1007 else 0b0000
bit_promo_1007 = 0b1000 if promo_tersedia_1007 else 0b0000

# OR (|) menggabungkan seluruh kondisi menjadi satu kode status
kode_status_1007 = bit_member_1007 | bit_belanja_1007 | bit_barang_1007 | bit_promo_1007

# AND (&) memeriksa apakah kondisi tertentu aktif pada kode status
cek_member_1007 = kode_status_1007 & 0b0001
cek_promo_1007 = kode_status_1007 & 0b1000


# XOR (^) membandingkan perbedaan status terhadap kode referensi
kode_referensi_1007 = 0b1011
xor_status_1007 = kode_status_1007 ^ kode_referensi_1007

# Bitwise shift sebagai tambahan (bukan wajib, pelengkap)
shift_status_1007 = kode_status_1007 << 1

# Hak akses pelanggan berdasarkan bit
member_access_1007 = bool(cek_member_1007)
promo_access_1007 = bool(cek_promo_1007)
free_shipping_access_1007 = promo_1007 == "GRATISONGKIR"

print("\n===== HAK AKSES PELANGGAN =====")
print(f"Kode Status (biner)        : {bin(kode_status_1007)}")
print(f"Kode Status (desimal)      : {kode_status_1007}")
print(f"Member Access              : {member_access_1007}")
print(f"Promo Access               : {promo_access_1007}")
print(f"Free Shipping Access       : {free_shipping_access_1007}")

#=====OPERASI BITWISE=====
print("\n=== OPERASI BITWISE =====")

print("\n===== Kode Status Transaksi =====")

#KODE STATUS
#0001 = member
#0010 = total belanja >= Rp 200000
#0100 = jumlah barang >= 3
#1000 = promo

#menggunakan OR (|)
kode_transaksi_1007 =  int(is_member_1007) << 0 | int(syarat_belanja_1007) << 1 | int(syarat_barang_1007) << 2 | int(promo_tersedia_1007) << 3
kode_referensi_1007 = int(is_member_1007) << 0 | int(syarat_belanja_1007) << 1 | int(promo_tersedia_1007) << 3

print(f"{format(int(is_member_1007) << 0, '04b')} | {format(int(syarat_belanja_1007) << 1, '04b')} | {format(int(syarat_barang_1007) << 2, '04b')} | {format(int(promo_tersedia_1007) << 3, '04b')}")
print(f"Kode Biner   : {format(kode_transaksi_1007, '04b')}") 
print(f"Kode Desimal : {kode_transaksi_1007}")


#=====PEMERIKSAAN STATUS=====
print("\n===== Pemeriksaan Status =====")


print("\nCek Member")

#menggunakan and (&)

print(f"{format(kode_transaksi_1007, '04b')} & {format(int(is_member_1007) << 0, '04b')}")
print(f"Hasil Biner   : {format((kode_transaksi_1007) & int(is_member_1007) << 0, '04b')}")
print(f"Hasil Desimal : {(kode_referensi_1007) & int(is_member_1007) << 0}") 

print("\nCek Promo")

print(f"{format(kode_transaksi_1007, '04b')} & {format(int(promo_tersedia_1007) << 3, '04b')}")
print(f"Hasil Biner   : {format((kode_transaksi_1007) & int(promo_tersedia_1007) << 3, '04b')}")
print(f"Hasil Desimal  : {(kode_transaksi_1007) & int(promo_tersedia_1007) << 3}")


#=====PERBANDINGAN STATUS=====
print("\n===== Perbandingan Status =====")

 # menggunakan XOR (^)

print(f"Kode Transaksi : {format(kode_transaksi_1007, '04b')}")
print(f"Kode Referensi : {format(kode_referensi_1007, '04b')}")
print(f"{format(kode_transaksi_1007, '04b')} ^ {format(kode_referensi_1007, '04b')}")
print(f"Hasil Biner    : {format((kode_transaksi_1007) ^ (kode_referensi_1007))}")
print(f"Hasil Desimal  : {(kode_transaksi_1007) ^ (kode_referensi_1007)}")


#======SHIFT GESER KIRI=====
print("\n===== Shift =====")

#bitwise kiri/ shift kiri (<<)

print(f"{format(kode_transaksi_1007,'04b')} << 1")
print(f"Hasil Biner   : {format((kode_transaksi_1007) << 1,'04b')}")
print(f"Hasil Desimal : {(kode_transaksi_1007) << 1}") 

print("\n===== SELESAI =====")
