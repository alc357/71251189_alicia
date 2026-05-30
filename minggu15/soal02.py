def palindrom(kalimat) : 
    kalimat = kalimat.replace(" ", "").lower()
    return cek(kalimat)

def cek (s) : 
    if len(s) <= 1 : 
        return True
    if s [0] != s[-1] : 
        return False 
    return cek(s[1:-1])

kalimat = input("Masukkan kalimat : ")
if palindrom(kalimat) : 
    print(f"{kalimat} adalah palindrom")
else : 
    print(f"{kalimat} bukan palindrom")
    
    
    