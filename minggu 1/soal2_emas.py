jumlah_gram_emas1 = 25 
harga_beli1 = 650000
harga_sekarang = 685000

jumlah_uang_beli1 = jumlah_gram_emas1 * harga_beli1
jumlah_uang_sekarang = harga_sekarang * jumlah_gram_emas1

Keuntungan1 = jumlah_uang_sekarang - jumlah_uang_beli1
persentase_keuntungan1 = (Keuntungan1/jumlah_uang_beli1) * 100

print(f"Keuntungan pertama Gerard adalah Rp. {Keuntungan1}")
print(f"Persentase dari keuntungan pertama Gerard adalah {persentase_keuntungan1:.2f}%")

jumlah_gram_emas2 = 15 
total_gram_emas = jumlah_gram_emas1 + jumlah_gram_emas2
harga_naik = 715000

jumlah_uang_beli2 = jumlah_gram_emas2 * harga_sekarang
total_uang_beli = jumlah_uang_beli1 + jumlah_uang_beli2
total_uang_sekarang = total_gram_emas * harga_naik

Keuntungan2 = total_uang_sekarang - total_uang_beli
persentase_keuntungan2 = (Keuntungan2/total_uang_beli)*100

print(f"Seluruh keuntungan Gerard adalah Rp. {Keuntungan2}")
print(f"Persentase dari keuntungan pertama Gerard adalah {persentase_keuntungan2:.2f}%")

