def tiga_terbaik (list_angka) : 
    if len(list_angka) < 3 : 
        return "List angka kurang dari 3"
    else : 
        list_angka = list(set(list_angka))
        list_angka.sort(reverse=True)
        return list_angka[:3]

angka = [3,9,4,8,0,1,6]
hasil = tiga_terbaik(angka)
print (f"3 angka terbaik adalah {hasil}")
    