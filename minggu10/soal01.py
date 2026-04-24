file1 = input("file pertama : ")
file2 = input("file kedua : ")

try : 
    handle1 = open(file1).readlines()
    handle2 = open(file2).readlines()
    
    jmlh_bris = max(len(handle1), len(handle2))
    berbeda = False 
    
    for i in range(jmlh_bris) : 
        if i < len(handle1) : 
            baris1 = handle1[i].rstrip()
        else : 
            baris1 = "Tidak ada baris"
        if i < len(handle2) : 
            baris2 = handle2[i].rstrip()
        else : 
            baris2 = "Tidak ada baris"
        if baris1 != baris2 :
            berbeda = True
            print("Perbedaan pada baris ke-" + str(i+1) + ":")
            print(" File 1 : " + baris1)
            print(" File 2 : " + baris2)
    if berbeda == False : 
        print("Kedua file sama persis")
except : 
    print("File tidak ditemukan")
    
   
    