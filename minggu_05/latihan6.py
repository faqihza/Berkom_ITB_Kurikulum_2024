# Latihan 6: Kalkulator Sederhana
''' 
Program ini menerima dua angka dan satu operator 
dari pengguna,kemudian melakukan operasi matematika 
sesuai dengan operator yang diberikan.
'''

# KAMUS
# operator: string
# angka_1: float
# angka_2: float

import os

print("Selamat datang di kalkulator:")


while True:
	operator = input("Masukkan operator (+, -, *, /) atau ketik q untuk keluar: ")
	
	os.system('clear')  # Gunakan 'cls' untuk Windows
	if operator == "q":
		break
	
	print(f"Baiklah, anda telah memilih: {operator}")
	print("Mari masukkan 2 angka yang akan dioperasikan")
	angka_1 = float(input("Angka 1: "))
	angka_2 = float(input("Angka 2: "))

	# kondisi untuk setiap operator
	if operator == "+":
		hasil = angka_1 + angka_2
	elif operator == "-":
		hasil = angka_1 - angka_2
	elif operator == "*":
		hasil = angka_1 * angka_2
	elif operator == "/":
		hasil = angka_1 / angka_2
	else:
		hasil = "Operator tidak valid"

	# print hasil
	print(f"{angka_1} {operator} {angka_2} = {hasil}")