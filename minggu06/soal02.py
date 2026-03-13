def ganjil (bawah, atas) : 
    if bawah < atas : 
        print(f"bawah = {bawah}, atas = {atas}. Karena bawah < atas, berarti dari kecil ke besar, maka hasilnya adalah: ", end='')
        if bawah % 2 == 0 : 
            bawah = bawah + 1
        else : 
            bawah = bawah 
            
        for i in range (bawah, atas+1, 2) :
            print (i, end='')
            if i == atas or i == atas-1 : 
                print('.')
            else : 
                print(', ', end='')
    elif bawah > atas : 
        print(f"bawah = {bawah}, atas = {atas}. Karena bawah > atas, berarti dari besar ke kecil, maka hasilnya adalah: ", end='')
        if bawah % 2 == 0 : 
            bawah = bawah-1
        else : 
            bawah = bawah
        
        for i in range (bawah, atas-1, -2) :
            print (i, end='')
            if i == atas or i == atas+1 : 
                print('.')
            else : 
                print(', ', end='')
    else : 
        if bawah % 2 == 0 : 
            print("2 angka inputanmu sama dan genap")
        else : 
            print(bawah)

bawah = int(input("Masukan batas bawah : "))
atas = int(input("Masukan batas atas : "))
ganjil(bawah,atas)

