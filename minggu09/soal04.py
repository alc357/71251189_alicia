kalimat = input("Masukan kalimat : ")

kalimat_list = kalimat.split()
terpendek = kalimat_list[0]
terpanjang = kalimat_list [0]
for kata in kalimat_list : 
    if len(kata) < len(terpendek) : 
        terpendek = kata
    if len(kata) > len(terpanjang) : 
        terpanjang = kata
print (f"terpendek : {terpendek}, terpanjang : {terpanjang}")
    