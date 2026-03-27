n = int(input("Masukan angka : "))

for i in range (n,0,-1) : 
    for j in range (i+1) : 
        if j == 0 : 
            hasil = 1
            for a in range (1, i+1) : 
                hasil = hasil * a 
            print(hasil, end=" ")
        else : 
            print(i-j+1, end=" ")
    print()
    
    
    