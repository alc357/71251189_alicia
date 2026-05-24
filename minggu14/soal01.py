n = int(input("Masukan jumlah kategori: "))

data_aplikasi = {} 
for i in range (n) : 
    nama_kategori = input("Masukkan nama kategori:")
    print("Masukkan 5 nama aplikasi di kategori", nama_kategori)
    aplikasi = []
    for j in range (5) : 
        nama_aplikasi = input("Nama aplikasi: ")
        aplikasi.append(nama_aplikasi)
        data_aplikasi[nama_kategori] = aplikasi
print("Data Aplikasi per Kategori")
print(data_aplikasi)

daftar_aplikasi_set = []
for a in data_aplikasi.values() : 
    daftar_aplikasi_set.append(set(a))
    
hitung = {}
for b in daftar_aplikasi_set : 
    for app in b : 
        if app in hitung : 
            hitung[app] += 1
        else : 
            hitung[app] = 1

hanya_satu = set()
for app, jml in hitung.items() : 
    if jml == 1 :
        hanya_satu.add(app)

print("Aplikasi hanya di satu kategori ")
print(hanya_satu)

if n>2 : 
    tepat_dua = set()
    for app, jml in hitung.items() :
        if jml == 2 : 
            tepat_dua.add(app)      
    print("Aplikasi tepat di dua kategori")
    print(tepat_dua)  
    