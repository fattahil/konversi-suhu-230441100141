phi = 3.14
luas_selimut = float(input("Masukkan luas selimut kerucut (cm^2): "))
tinggi = float(input("Masukkan tinggi kerucut (cm): "))
garis_pelukis = float(input("Masukkan garis pelukis kerucut (cm): "))

r = luas_selimut / (phi * garis_pelukis)

volume = (1/3) * phi * (r**2) * tinggi

print("Volume kerucut adalah" volume "cm^3/liter")
