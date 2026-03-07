def cek_digit_belakang (a,l,c) :
    digit_a = a % 10 
    digit_l = l % 10 
    digit_c = c % 10 
    if (digit_a == digit_l) or (digit_a == digit_c) or (digit_l == digit_c) : 
        return "True" 
    else : 
        return "False"
    
a1 = int(input("angka 1 : "))
a2 = int(input("angka 2 : "))
a3 = int(input("angka 3 : "))
    
print(cek_digit_belakang(a1,a2,a3))