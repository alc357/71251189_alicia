n = int(input("Masukan angka : "))

if n <=2 : 
    print("Inputanmu terlalu kecil")
else : 
    for i in range (n-1,1,-1) : 
        for j in range (2,i) : 
            if i % j  == 0 : 
                break 
        else : 
                print(f"Bilangan prima terdekat <{n} adalah {i}")
                break 
            
            
            
        


            