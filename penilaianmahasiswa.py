
ulang = "y"
while ulang=="y" or ulang=="Y":
    print ("================================")
    print ("      Penilaian Mahasiswa       ")
    print ("================================")

    m = input(">> Masukkan Nilai = ")

    if int(m)>=91 and int(m)<=100:
        penilaian="A"
    elif int(m)>=81 and int(m)<=91:
        penilaian="B"
    elif int(m)>=71 and int(m)<=81:
        penilaian="C"
    else:
        penilaian="D"
    print(penilaian)
    ulang=input(">>ulang program? Y/T = ")
    if ulang=="t" or ulang=="T":
        break
    