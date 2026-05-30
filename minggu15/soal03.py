def ganjil (n) : 
    if n == 1 : 
        return 1 
    return (2*n-1) + ganjil(n-1)

n = int(input("Masukan jumlah suku (n) : "))
hasil = ganjil(n)

deret = [str(2 * i -1) for i in range (1,n+1)] 
print("deret :", "+".join(deret))
print (f"Jumlah : {hasil}")


