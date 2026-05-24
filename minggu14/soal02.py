print("Konversi List jadi Set")
print("-" *25)
lst_data = [1,2,3,4,5,6,7,8,8]
print("Data sebelum diubah :", lst_data)
print("tipe sebelum diubah :", type(lst_data))
set_data = set(lst_data)
print("Data setelah diubah :", set_data)
print("Tipe setelah diubah :", type(set_data))
print()

print("Konversi Set jadi List")
print("-"* 25)
set_data2 = {5,6,7,8,25,30}
print("Data sebelum diubah :", set_data2)
print("Tipe sebelum diubah :", type(set_data2))
lst_data2 = list(set_data2)
print("Data setelah diubah :", lst_data2)
print("Tipe data setelah diubah :", type(lst_data2))
print()

print("Konversi Tuple jadi Set")
print("-" * 25)
tpl_data = ("apel", "semangka", "mangga","pisang", "jeruk")
print("Data sebelum diubah :", tpl_data)
print("Tipe sebelum diubah :", type(tpl_data))
set_data3 = set(tpl_data)
print ("Data setelah diubah :", set_data3)
print("Tipe data setelah diubah :", type(set_data3))
print()

print("Konversi Set jadi Tuple")
print("-" * 25)
set_data4 = {100,200,300,400,500}
print("Data sebelum diubah :", set_data4)
print("Tipe sebelum diubah :", type(set_data4))
tpl_data2 = tuple(set_data4)
print ("Data setelah diubah :", tpl_data2)
print("Tipe data setelah diubah :", type(tpl_data2))

