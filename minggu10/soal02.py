import re
namafile = input("Nama file : ")
try : 
    handle = open(namafile)
    for line in handle : 
        line = line.rstrip()
        soal, jawaban = line.split(" || ")
        print (soal)
        jawaban_user = input ("Jawab: ")
        jawaban_oke = re.sub(r'[ -]', '', jawaban.strip().lower())
        jawaban_user_oke = re.sub(r'[ -]', '', jawaban_user.strip().lower())
        if jawaban_user_oke == jawaban_oke : 
            print("Jawaban benar!")
        else : 
            print("Jawaban salah!")
except : 
    print("File tidak ditemukan!")