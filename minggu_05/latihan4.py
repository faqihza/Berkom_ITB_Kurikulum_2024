user_input = int(input("Masukkan index akhir: "))

hasil_jumlah = 0
for i in range(1,user_input+1):
	hasil_jumlah = hasil_jumlah + i

print(f"hasil jumlah = {hasil_jumlah}")

hasil_kali = 1
for i in range(1,user_input+1):
	hasil_kali = hasil_kali * i

print(f"hasil kali = {hasil_kali}")