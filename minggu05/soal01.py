def cek_angka(a,l,c) : 
    if (a != l != c) and ((a+l == c) or (a+c == l)or (l+c == a)) : 
        return True
    else :
        return False

a1 = int(input("Angka 1 : "))
a2 = int(input("Angka 2 : "))
a3 = int(input("Angka 3 : "))

print(cek_angka(a1,a2,a3))