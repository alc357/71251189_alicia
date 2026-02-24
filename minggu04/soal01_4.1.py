input_user = input("Masukkan suhu tubuh: ")

try : 
    suhu = int(input_user)
    if suhu >= 38 :
        print("Anda demam")
    else : 
        print("Anda tidak demam")
except : 
    print("Data anda tidak sesuai")