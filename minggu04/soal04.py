input_1 = input ("Masukan panjang sisi 1 : ")
input_2 = input ("Masukan panjang sisi 2 : ")
input_3 = input("Masukan panjang sisi 3 : ")

try : 
    sisi_1 = int(input_1)
    sisi_2 = int(input_2)
    sisi_3 = int(input_3)
    if (sisi_1 == sisi_2) and (sisi_2 == sisi_3) : 
        print("3 sisi sama")
    elif (sisi_1 == sisi_2) or (sisi_1 == sisi_3) or (sisi_2 == sisi_3) : 
        print("2 sisi sama")
    else :
        print("Tidak ada yang sama")
except : 
    print("Mungkin data yang kamu masukan ada yang bukan angka")