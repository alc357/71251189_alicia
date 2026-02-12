# membuat variabel untuk menyimpan input pengguna tentang gaji perjam dan jam kerja
gaji_per_jam = int(input("Berapa Gaji yang diinginkan Budi tiap jamnya? "))
jumlah_jam_kerja = int(input("Berapa jam kerja yang diinginkan Budi tiap minggu? "))
jumlah_minggu = 5

# menghitung total gaji Budi selama 5 minggu bekerja dan setelah dipotong pajak
total_gaji = round((gaji_per_jam * jumlah_jam_kerja*jumlah_minggu),2)
setelah_potong_pajak = round(total_gaji - (total_gaji * (14/100)), 2)

# menghitung uang belanja dan alat tulis 
uang_belanja = round(setelah_potong_pajak * (10/100), 2)
uang_alat_tulis = round(setelah_potong_pajak * (1/100), 2)
total_belanja = uang_belanja + uang_alat_tulis

# menghitung uang setelah belanja 
uang_setelah_belanja = setelah_potong_pajak - total_belanja

# menghitung uang sedekah (diterima anak yatim dan kaum dhuafa)
uang_sedekah = round(uang_setelah_belanja* (25/100), 2)
untuk_yatim = round(uang_sedekah * (30/100), 2)
untuk_kaum_dhuafa = round((uang_sedekah-untuk_yatim), 2)

# memberikan output 
print(f"Pendapatan Budi selama libur musim panas sebelum melakukan pembayaran pajak adalah Rp {total_gaji}")
print(f"Pendapatan Budi selama libur musim panas setelah melakukan pembayaran pajak adalah Rp {setelah_potong_pajak}")
print(f"Total uang yang Budi habiskan untuk membeli pakaian dan aksesoris adalah Rp {uang_belanja}")
print(f"Total uang yang Budi habiskan untuk membeli alat tulis adalah Rp {uang_alat_tulis}")
print(f"Uang yang Budi sedekahkan adalah Rp {uang_sedekah}")
print(f"Uang sedekah Budi yang diterima anak yatim adalah Rp {untuk_yatim}")
print(f"Uang sedekah Budi yang diterima kaum dhuafa adalah Rp {untuk_kaum_dhuafa}")