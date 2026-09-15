print ("=== SISTEM REGISTRASI PRAKTIKAN ALPRO 2026 ===")

nama_1007 = input(str("Masukkan Nama Mahasiswa : "))
jenis_kelamin_1007 = input ("Masukkan Jenis Kelamin (L/P) : ")
umur_1007 = int(input("Masukkan Umur : "))
skor_tes_awal_1007 = float(input("Masukkan Skor Tes Awal : "))

print("\n=== DATA PRAKTIKAN & HASIL PEMERIKSAAN ===")

alamat_1007 = """
Komplek wisma bumi mas,
Kec. Kuranji,
Kota Padang """
id_token_sinyal = 100+3j

print("Nama Mahasiswa :", nama_1007, "|", "Tipe :", type(nama_1007))
print("Jenis Kelamin :", jenis_kelamin_1007, "|", "Tipe :", type(jenis_kelamin_1007))
print("Alamat Domisili :", alamat_1007, "|", "Tipe :", type(alamat_1007))
print("Umur :", umur_1007, "tahun", "|", "Tipe :", type(umur_1007))
print("Skor Tes Awal :", skor_tes_awal_1007, "|", "Tipe :", type (skor_tes_awal_1007))
print("ID Token Sinyal :", id_token_sinyal, "|", "Tipe :", type (id_token_sinyal))

print("\n=== STATUS KELULUSAN PRAKTIKUM ===")

batas_1007 = 75.0

print("Batas Minimum Nilai:", batas_1007)
if skor_tes_awal_1007 >= batas_1007:
    hasil_1007 = True
else:
    hasil_1007 = False
print("Apakah dinyatakan lulus?:", hasil_1007, "|", "Tipe :", type (hasil_1007))