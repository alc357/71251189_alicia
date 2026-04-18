import re 
import random 
print("masukan teks yang mengandung email (ketik - jika sudah) : ")
semua = []
while True : 
    baris = input()
    if baris == "-" : 
        break 
    semua.append(baris)
teks = "\n".join(semua)

daftar_email = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',teks)
karakter = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
if len(daftar_email) == 0 : 
    print("tidak ditemukan email") 
else : 
    for email in daftar_email : 
        username = email.split('@')[0]
        password =''
        for i in range (8) : 
            password += random.choice(karakter)
        print (f"{email} username : {username} , password: {password}")