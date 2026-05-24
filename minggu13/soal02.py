data = ('Alicia Luna Santoso', '71251189','Muntilan, Magelang')
nama,nim,alamat = data
tpl_nim = tuple(nim)
nama_depan = nama.split()[0]
tpl_depan = tuple(nama_depan[1:])
nama_split = nama.split()
tpl_balik = tuple(nama_split[::-1])
print(f"Data : {data}")
print()
print(f"NIM : {nim}")
print(f"NAMA : {nama}")
print(f"ALAMAT : {alamat}")
print()
print(f"NIM : {tpl_nim}")
print()
print(f"NAMA DEPAN : {tpl_depan}")
print()
print(f"NAMA TERBALIK : {tpl_balik}")


