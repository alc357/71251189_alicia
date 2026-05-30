def digit(bilangan) : 
    bilangan = str(bilangan)
    if len(bilangan) == 1 : 
        return int(bilangan)
    return int(bilangan[0]) + digit(bilangan[1:])

bilangan = input("Masukkan bilangan : ")
hasil = digit(bilangan)

tampil = "+".join(list(bilangan))
print(f"Penjumlahan : {tampil} = {hasil}")


