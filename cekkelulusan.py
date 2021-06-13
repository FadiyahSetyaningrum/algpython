
ulang = "y"
while ulang=="y" or ulang=="Y":
    print ("================================")
    print ("          Cek Kelulusan         ")
    print ("================================")

    n = input(">> Masukkan Nilai = ")

    if int (n)>60:
        sts = "Lulus"
    else:
        sts = "Tidak Lulus"
    print(sts)
    ulang=input(">>ulang program? Y/T = ")
    if ulang=="t" or ulang=="T":
        break