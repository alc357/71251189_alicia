tinggi = int(input("masukan tinggi : "))
lebar = int(input("masukan lebar : "))

angka = 1
for i in range (1,tinggi+1) : 
    for j in range (1,lebar+1) : 
        print(angka, end=" ")
        angka = angka+1
    print()
    
    