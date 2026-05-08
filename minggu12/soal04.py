fname = input("masukan nama file : ")

try : 
    fhandle = open(fname)
except FileNotFoundError : 
    print("File tidak bisa dibuka : ", fname)
    exit()
    
domain_dct = {}
for line in fhandle : 
    if line.startswith("From ") : 
        kata = line.split()
        email = kata[1]
        
        domain= email.split('@')[1]
        if domain not in domain_dct : 
            domain_dct[domain] = 1
        else : 
            domain_dct[domain] += 1 
            
print(domain_dct)        