input_user = input("Masukan suatu bilangan : ")

try : 
    bilangan = int(input_user)
    if bilangan > 0 :
        print("Positif")
    elif bilangan < 0 : 
        print ("Negatif")
    elif bilangan == 0 :
        print ("Nol")
except : 
    print("data anda tidak sesuai")