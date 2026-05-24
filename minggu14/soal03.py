import string 

file1 = input("Masukkan nama file 1 : ").strip()
file2 = input("Masukkan nama file 2 : ").strip()
print()
try : 
    handle1 = open(file1).read()
    handle2 = open(file2).read()
    for tanda in string.punctuation : 
        handle1 = handle1.replace(tanda, " ")
    set1 = set(handle1.lower().split())
    for tanda in string.punctuation : 
        handle2 = handle2.replace(tanda, " ")
    set2 = set(handle2.lower().split())
    sama = set1 & set2
    semua = set1 | set2
    print(f"Kata di file {file1} : {set1}")
    print("_" * 40)
    print(f"Kata di file {file2} : {set2}")
    print("_" * 40)
    print(f"Semua kata yang ada di file {file1} atau {file2} : {semua}")
    print("_" * 40)
    print(f"Kata yang muncul di kedua file : {sama}")
except FileNotFoundError as e:
    print(f"ERROR : File tidak ditemukan! Detail: {e}")
except Exception as e : 
     print(f"ERROR: File tidak bisa dibaca! Detail: {e}")
     
     
     
    