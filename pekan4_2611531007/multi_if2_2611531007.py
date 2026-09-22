# Buat file dengan nama multi_if2_NIM.py
# Buat program untuk kondisional if 
# Nama variabel ditambah 4 digit nim terakhir, contoh: total_belanja_1234
# Program ini menggunakan fungsi input ()
# Program ini menghitung diskon belanja

# Input dari user
total_belanja_1007 = float(input("Masukkan total belanja (Rp): "))

# Input status member (mengecek apakah user mengetik 'y' atau 'ya')
input_member_1007 = input ("Apakah Anda Member? (y/t):").strip().lower
is_member_1007 = input_member_1007 in ["y", "ya"]

# Input status kode promo (mengecek apakah user mengetik 'y' atau 'ya')
input_promo_1007 = input("Apakah kode promo calid? (y/t):").strip().lower
kode_promo_valid_1007 = input_promo_1007 in ["y", "ya"]

total_diskon_persen_1007 = 0

# Multi if terpisah: Setiap kondisi diperiksa secara independen
# Diskon bisa ditumpuk (akumulasi) jika memenuhi beberapa syarat sekaligus
if total_belanja_1007 > 1000000:
    total_diskon_persen_1007 += 10 # Diskon belanjan besar

if is_member_1007:
    total_diskon_persen_1007 += 5 # Diskon member

if kode_promo_valid_1007:
    total_diskon_persen_1007 += 15 # Diskon voucher

# Menghitung nominal diskon dan total bayar
nominal_diskon_1007 = total_belanja_1007 * (total_diskon_persen_1007 / 100)
total_bayar_1007 = total_belanja_1007 - nominal_diskon_1007

# Output Hasil
print("\n--- Rincian Pembayaran ---")
print(f"Total Diskon  : {total_diskon_persen_1007}% (Rp {nominal_diskon_1007:,.0f})")
print(f"Total Bayar   : Rp {total_bayar_1007:,.0f}")

print(f"Total diskon yang Anda dapatkan: {total_diskon_persen_1007}%")
# Output: Total diskon yang Anda dapatkan : 30% jika belanja > 1 juta , member, kode promo valid