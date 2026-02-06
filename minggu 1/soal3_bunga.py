uang_masuk = 200000000
saldo_minimal = 400000000
bunga_tahunan = 10/100

tahun_menabung = 0
saldo = uang_masuk 

while saldo < saldo_minimal:
    saldo += saldo * bunga_tahunan
    tahun_menabung +=1
    
print(f"Erika harus menabung selama {tahun_menabung:} tahun")