print("=== SISTEM LOKET ALPRO ADVENTURE PARK ===")
nama_1007 = input("Masukkan Nama Pengunjung            :")
umur_1007 = int(input("Input Umur Anda                     :"))
sim_1007 = input("Apakah Anda Sudah Punya SIM C (y/t) :")[0].lower()

print("Masukkan Nama Pengunjung            :",nama_1007)
print("Input Umur Anda                     :",umur_1007)
print("Apakah Anda Sudah Punya SIM C (y/t) :",sim_1007)

print("\nPilihan Paket Wahana (1-5):")
print("  1. Safari Rimba         (Rp 50,000)")
print("  2. Arung Jeram          (Rp 75,000)")
print("  3. Motor ATV Ekstrim    (Rp 120,000)")
print("  4. Roller Coaster Kilat (Rp 100,000)")
print("  5. All-Access VIP       (Rp 220,000)")

paket_1007 = int(input("\nMasukkan Nomor Paket (1-5)    :"))
jumlah_1007 = int(input("Masukkan Jumlah Tiket         :"))
member_1007 = input("Apakah Anda Member? (y/t)     :")[0].lower()
promo_1007 = input("Apakah Kode Promo Valid: (y/t):")[0].lower()

if jumlah_1007 <= 0:
    print("Kuota Tiket Tidak Valid")

match paket_1007:
    case 1:
        nama_wahana_1007 = ("Wahana Safari Rimba")
        harga_1007 = 50000
    case 2:
        nama_wahana_1007 = ("Wahana Arung Jeram")
        harga_1007 = 75000
    case 3 :
        nama_wahana_1007 = ("Wahana Motor ATV Ekstrim")
        harga_1007 = 120000
    case 4 :
        nama_wahana_1007 = ("Wahana Roller Coaster Kilat")
        harga_1007 = 100000
    case 5 :
        nama_wahana_1007 = ("Wahana All-Access VIP")
        harga_1007 = 220000
    case _:
        print("\nPaket Wahana Tidak Valid")
        exit()

print("\n--- KELAYAKAN PENGENDARA WAHANA ---")

if paket_1007 == 3 and umur_1007 >= 17 and sim_1007 == 'y':
    status_1007 = "Anda sudah dewasa dan boleh mengendarai ATV sendiri."
elif paket_1007  == 3 and umur_1007 >= 17 and sim_1007 != 'y':
    status_1007 = "Anda sudah dewasa tetapi tidak boleh bawa motor ATV (wajib didampingi instruktur)."
elif paket_1007 == 3 and umur_1007 < 17 and sim_1007 == 'y':
    status_1007 = "Identitas tidak valid: Belum cukup umur memiliki SIM."
elif paket_1007 != 3 and umur_1007 >= 10:
    status_1007 = "Anda cukup umur untuk menikmati wahana ini."
else:
    status_1007 = "Anda belum cukup umur dan tidak boleh bawa motor ATV."

print(f"Status Akses:", status_1007)

subtotal_1007 = harga_1007 * jumlah_1007
totaldiskon_1007 = 0

if subtotal_1007 >= 200000:
    totaldiskon_1007 += 10
if member_1007 in  ['y', 'ya']:
    totaldiskon_1007 += 5
if promo_1007 in ['y', 'ya']:
    totaldiskon_1007 += 15
if jumlah_1007 >= 5:
    totaldiskon_1007 += 5

nominal_diskon_1007 = subtotal_1007 * (totaldiskon_1007 / 100)
total_bayar_1007 = subtotal_1007 - nominal_diskon_1007

if total_bayar_1007 > 300000:
    catatan_layanan_1007 = "Selamat! Anda berhak mendapatkan Souvenir Gratis."
else:
    catatan_layanan_1007 = "Terima kasih telah berkunjung."
 
print("\n--- Rincian Pembayaran ---")
print(f"Subtotal Belanja  : Rp {subtotal_1007:,.0f}")
print(f"Total Diskon      : {totaldiskon_1007}% (Rp {nominal_diskon_1007:,.0f})")
print(f"Total Bayar       : Rp {total_bayar_1007:,.0f}")
print(f"Catatan Layanan   : {catatan_layanan_1007}")
print("Program Selesai")
