import math

def luas_lingkaran(jari_jari):
	luas = math.pi * (jari_jari**2)
	return luas

R1 = 1
L1 = luas_lingkaran(R1)
L2 = luas_lingkaran(4)
L3 = luas_lingkaran(1000000)

print(L1)