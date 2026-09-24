# Input: Besar sudut dalam derajat
# Aturan Keputusan: Rentang yang sah > 0 dan < 180, lalu klasifikasi jenis sudutnya
# Output: Jenis sudut atau pesan error penolakan

sudut = float(input("Besar sudut dalam derajat: "))

if sudut <= 0 or sudut >= 180:
    print("Masukan ditolak: sudut harus lebih dari 0 dan kurang dari 180.")
elif sudut < 90:
    print("Sudut lancip")
elif sudut == 90:
    print("Sudut siku-siku")
else:
    print("Sudut tumpul")
    