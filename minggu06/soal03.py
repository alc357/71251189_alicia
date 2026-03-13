def IPS(jmlh_matkul) : 
    nilaimu = 0
    for i in range (jmlh_matkul) : 
        abjad = (input(f'Nilai MK {i+1} : '))
        if abjad == 'A' : 
            poin = 3*4
        elif abjad == 'B' : 
            poin = 3*3
        elif abjad == 'C' : 
            poin = 3*2
        elif abjad == 'D' : 
            poin = 3*1 
        total = poin + nilaimu 
        nilaimu = total 
    ips_semester = round((nilaimu /(jmlh_matkul * 3)),2)
    print(f'Nilai IPS anda semester ini {ips_semester}')
    
jmlh_matkul = int(input("Berapa jumlah mata kuliah? "))
IPS(jmlh_matkul)

