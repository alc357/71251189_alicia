import re 
namafile = input("Nama file : ")
handle = open(namafile).read()

kata = re.findall(r'\b\w+\b', handle.lower())
unik = list(set(kata))
unik.sort()

print("Daftar kata unik : ")
for i in range (len(unik)): 
    print(f"{i+1}. {unik[i]}")
    
    