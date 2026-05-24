inp_user = eval(input("Masukan tuple angka : "))

if not isinstance(inp_user, tuple) : 
    print("inputmu bukan tuple heii")
else : 
    sama = True
    if len(inp_user) == 0 :
        print(sama)
        print("(Tapi Tuple mu kosong)")
    elif len(inp_user) == 1 : 
        print(sama)
        print("(Tapi Tuple mu hanya memiliki 1 angka)") 
    else : 
        for i in range (len(inp_user)-1) :
            if inp_user[i] != inp_user[i+1] : 
                sama = False
                break
        print(sama)

