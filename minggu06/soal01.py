def perkalian (a,b) : 
    print(f"{a} x {b} = ", end='')
    
    for i in range (a) : 
        print (f"{b}", end='')
        
        if i < a-1 : 
            print (' + ', end= '')
        else : 
            print(' =', end='')
    
    jumlah = 0 
    for i in range (a) : 
        hasil = jumlah + b
        jumlah = hasil 
    print (f" {hasil}.")

a = int(input("Masukan bilangan pertama : "))
b = int(input("Masukan bilangan kedua : "))
perkalian(a,b)



