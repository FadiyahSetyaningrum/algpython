
ulang = "y"
while ulang=="y" or ulang=="Y":
    print ("=================================")
    print ("            Cek Usia             ")
    print ("=================================")

    u = input(">> Masukkan Usia = ")

    if int(u)>=60:
        sts="Lansia"
    elif int(u)>=35 and int(u)<=59:
        sts="Dewasa"
    elif int(u)>=18 and int(u)<=34:
        sts="Pemuda"
    elif int(u)>=15 and int(u)<=17:
        sts="Remaja"
    else:
        sts="anak"
    print(sts)

    ulang=input(">>ulang program? Y/T = ")
    if ulang=="t" or ulang=="T":
        break