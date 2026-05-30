def prima (n, i=2) : 
    if n < 2 : 
        return False 
    if i * i > n :
        return True
    if n % i == 0 : 
        return False 
    return prima(n,i+1)

n = int(input("Masukan bilangan : "))
if prima(n) :
    print(f"{n} adalah bilangan prima")
else : 
    print(f"{n} bukan bilangan prima")
    
    