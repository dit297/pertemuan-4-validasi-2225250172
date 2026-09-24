# Input: Nilai akhir
# Aturan Keputusan: Konversi rentang nilai menjadi predikat A-E
# Output: Predikat nilai

nilai = float(input("Nilai akhir (0-100): "))

if nilai >= 85:
    predikat = "A"
elif nilai >= 70:
    predikat = "B"
elif nilai >= 60:
    predikat = "C"
elif nilai >= 50:
    predikat = "D"
else:
    predikat = "E"

print(f"Nilai {nilai:.2f} memperoleh predikat {predikat}.")


