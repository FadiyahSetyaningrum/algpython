
ulang = "y"
while ulang=="y" or ulang=="Y":
    print("========================================")
    print("         Menampilkan Nilai Huruf        ")
    print("========================================")

    h = input(">> Masukkan Nilai = ")

    if int(h)>=80:
        nilaihuruf="Baik Sekali"
    elif int(h)>=65:
        nilaihuruf="Baik"
    elif int(h)>=55:
        nilaihuruf="Cukup"
    elif int(h)>=40:
        nilaihuruf="Kurang"
    else:
        nilaihuruf="Kurang Sekali"
    print(nilaihuruf)

    ulang=input(">>ulang program? Y/T = ")
    if ulang=="t" or ulang=="T":
        break