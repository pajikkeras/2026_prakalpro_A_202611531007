is_lulus_1007 = True
is_cumalude_1007 = True

nilai_1007 = 99
batas_lulus_1007 = 75

status_kelulusan_1007 = nilai_1007 >= batas_lulus_1007

print("=== Check Kelulusan ===")
print("Nilai: ", nilai_1007)
print("Apakah Lulus?:", status_kelulusan_1007)
if is_lulus_1007 and is_cumalude_1007:
    print("Selamat, Anda lulus dengan prediket Cum Laude!")