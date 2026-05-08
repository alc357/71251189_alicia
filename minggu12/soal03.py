fname = input("Nama File : ")

try : 
    fhandle = open(fname)
except FileNotFoundError : 
    print("File tidak bisa dibuka:", fname)
    exit()
    
jumlah = {}
for line in fhandle : 
    if line.startswith("From ") : 
        words = line.split()
        email = words[1]
        if email not in jumlah : 
            jumlah[email] = 1
        else : 
            jumlah[email] += 1
print(jumlah)