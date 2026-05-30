def faktorial (n) : 
    if n == 0 or n == 1 : 
        return 1 
    return n * faktorial (n-1)

def kombinasi (n,r) : 
    if r==0 or r == n : 
        return 1 
    return kombinasi(n-1, r-1) + kombinasi(n-1,r)

n = int(input("Masukkan nilai n : "))
r = int(input("Masukkan nilai r : "))

if r > n : 
    print("r tidak boleh lebih besar dari n")
else : 
    hasil = kombinasi(n,r)
    print(f"C({n}, {r}) = {n}! / {r}! x ({n}-{r})!)")
    print(f"C({n}, {r}) = {hasil}")
    
    
    