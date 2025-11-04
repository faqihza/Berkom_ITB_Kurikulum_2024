# macam-macam argument

def jumlah(list_data):
	hasil_jumlah = 0
	for angka in list_data:
		hasil_jumlah += angka
	
	list_data[2]=10
	return hasil_jumlah

data = [1,2,3,4,5]
print(f"data before = {data}")

hasil = jumlah(data)
print(f"hasil jumlah = {hasil}")

print(f"data after = {data}")