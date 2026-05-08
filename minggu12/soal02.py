lst1 = eval(input("List key : "))
lst2 = eval(input("List Value : "))

dct = {}
for i in range (len(lst1)) : 
    dct[lst1[i]] = lst2[i]

print(dct)

