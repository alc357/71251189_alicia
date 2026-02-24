input_user = input("Masukan bilangan yang ingin kamu cek (dalam angka) : ")
try : 
    bulan = int(input_user)
    if bulan == 2 : 
        print(f"Jumlah hari pada bulan {bulan} adalah 29")
    elif (bulan < 8 and bulan % 2 == 1) or (bulan >= 8 and bulan % 2 == 0) : 
        print(f"Jumlah hari pada bulan {bulan} adalah 31")
    elif (bulan < 8 and bulan % 2 == 0) or (bulan >=8 and bulan % 2 == 1) : 
        print(f"Jumlah hari pada bulan {bulan} adalah 30")
except: 
    print("mungkin yang kamu input bukan angka :)")