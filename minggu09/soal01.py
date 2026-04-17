k1 = input("Masukan kata pertama : ").lower()
k2 = input("Masukan kata kedua : ").lower()

if len(k1) == len(k2) : 
    k1_urut = sorted(k1)
    k2_urut = sorted(k2)
    if k1_urut == k2_urut : 
        print(f"{k1} dan {k2} adalah anagram")
    else : 
        print(f"{k1} dan {k2} bukan anagram")
else : 
    print(f"{k1} dan {k2} bukan anagram")
    
    
    