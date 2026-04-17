import re 
from datetime import datetime 

teks = input("Masukan kalimat yang mengandung tanggal dengan format YYYY-MM-DD : ")
dftr_tgl = re.findall(r'\d{4}-\d{2}-\d{2}', teks)
tgl_skr = datetime.now().date()
if len (dftr_tgl) == 0 : 
    print("Tidak ada tanggal yang sesuai format")
else : 
    for tgl_str in dftr_tgl : 
        tgl_obj = datetime.strptime(tgl_str, '%Y-%m-%d')
        selisih = (tgl_skr - tgl_obj.date()).days
        print(f"{tgl_str} 00:00:00 selisih {selisih} hari")
