# Program kalkulator
# Program ini akan mengkalkulasi operasi matematika

# Kamus
# angka1 : integer
# angka2 : integer
# hasil_jumlah : integer
# hasil_kurang : integer
# hasil_kali : integer
# hasil_bagi : integer
# hasil_pangkat : integer
# hasil_division : integer
# hasil_modulo : integer

# algoritma

print("Program Penjumlahan")
print("===================")

angka1 = int(input("angka 1 = "))
angka2 = int(input("angka 2 = "))

hasil_jumlah = angka1 + angka2
hasil_kurang = angka1 - angka2
hasil_kali = angka1 * angka2
hasil_bagi = angka1 / angka2
hasil_pangkat = angka1 ** angka2
hasil_division = angka1 // angka2
hasil_modulo = angka1 % angka2

print("hasil jumlah =",hasil_jumlah)
print("hasil kurang =",hasil_kurang)
print("hasil kali =",hasil_kali)
print("hasil bagi =",hasil_bagi)
print("hasil pangkat =",hasil_pangkat)
print("hasil division =",hasil_division)
print("hasil modulo =",hasil_modulo)