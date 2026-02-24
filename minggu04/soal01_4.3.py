input_user_a = input("Masukan bilangan pertama : ")
input_user_b = input("Masukan bilangan kedua : ")
input_user_c = input("Masukan bilangan ketiga : ")

try : 
    a = int(input_user_a)
    b = int(input_user_b)
    c = int(input_user_c)
    if a > b and a > c : 
        print (f"Terbesar : {a}")
    elif b > a and b > c : 
        print (f"Terbesar : {b}")
    elif c > a and c > b : 
        print (f"Terbesar : {c}")
except : 
    print("Ada datamu yang tidak sesuai, mungkin ada yang bukan angka")
