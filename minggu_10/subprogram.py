def print_barang(barang_arg,harga_arg,jumlah_arg):
	print(f"{barang_arg} - Harga: Rp {harga_arg} | Jumlah: {jumlah_arg}")

def jumlah(list_data):
	hasil_jumlah = 0
	for angka in list_data:
		hasil_jumlah += angka
	
	list_data[2]=10
	return hasil_jumlah

def luas_segitiga(alas,tinggi):
	luas = 0.5*alas*tinggi
	return luas