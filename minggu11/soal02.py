print("Masukkan bilangan (ketik 'done' untuk selesai) :")
bilangan =[]
while True : 
    masukan = input("bilangan : ")
    if masukan.lower() == "done" : 
        break 
    angka = float(masukan)
    bilangan.append(angka)
if len(bilangan) == 0 : 
    print("Kamu tidak memasukan bilangan")
else : 
    total = sum(bilangan)
    jumlah = len(bilangan)
    rata2 = total/jumlah
    print(f"Rata-rata : {rata2}")
    
    