nama_file = input("Enter a file name: ")

try : 
    handle = open(nama_file)
    hitung_jam = {}
    for baris in handle :
        if baris.startswith('From ') : 
            kata = baris.split()
            if len(kata) >= 6 : 
                waktu = kata[5]
                jam = waktu.split(':')[0]
                if jam not in hitung_jam : 
                    hitung_jam[jam] = 1
                else : 
                    hitung_jam[jam] += 1 
    handle.close()
    
    for jam in sorted(hitung_jam.keys()) : 
        print(jam, hitung_jam[jam])
        
except FileNotFoundError : 
    print("file tidak ditemukan")
    
    