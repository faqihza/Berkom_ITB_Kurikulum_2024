user_input = int(input("masukkan angka: "))

for i in range(1,user_input+1):
	print(i*"*")

print("\n")

for n in range(1,user_input+1):
	y = user_input - n + 1
	x = 2*n - 1
	print( y * " ", x * "*" )