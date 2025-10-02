print("Deret Fibonacci:")
user_input = int(input("Masukkan index akhir: "))

angka_fibo_1 = 1
angka_fibo_2 = 1

print(f"index-1 = {angka_fibo_1}")
print(f"index-2 = {angka_fibo_2}")

for i in range(3,user_input+1):
    angka_fibo_0 = angka_fibo_1 + angka_fibo_2
    print(f"index-{i} = {angka_fibo_0}")
    # mari geser
    angka_fibo_2 = angka_fibo_1
    angka_fibo_1 = angka_fibo_0