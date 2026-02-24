input_user = input("Masukan suatu bilangan : ")

try : 
    bilangan = int(input_user)
    output = "Positif" if bilangan > 0 else "Negatif" if bilangan < 0 else "Nol"
    print(output)
except : 
    print("Sepertinya datamu bukan angka :)")
    
    
#sekalian pake try and except ya kak hehe :