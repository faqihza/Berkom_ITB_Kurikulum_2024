# subrutin - tidak menghasilkan output / hasil perhitungan


def print_barang(barang_arg,harga_arg,jumlah_arg):
	print(f"{barang_arg} - Harga: Rp {harga_arg} | Jumlah: {jumlah_arg}")

list_barang = ["iphone","iwatch","imac"]
list_harga = [10000,100,50]
list_jumlah = [5,10,6]

for index in range(0,len(list_barang)):
	print_barang(list_barang[index],list_harga[index],list_jumlah[index])