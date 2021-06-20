ulang = "y"
while ulang=="y" or ulang=="Y":   
    
    print ("====================================================")
    print ("              BENGKEL MOTOR UD.MATAHARI             ")
    print ("====================================================")
    print (" Kode = a = Duration SW20 1L")
    print (" Kode = b = Castrol Magnatec 1L")
    print (" Kode = c = Federal Supreme XX 1L")
    print (" Kode = d = Yamalube 1L")
    print (" Kode = e = Shell 1L")
    

    OliMotor = ['Duration SW20 1L','Castrol Magnetic 1L','Federal Supreme XX 1L','Yamalube 1L','Shell 1L']
    harga = [53000,50000,54000,45000,46000]
    PPN = 1/100
    
    pilihan = input(" Masukkan Kode  = ")

    if pilihan=="a":
        idx = 0
    elif pilihan=="b":
        idx = 1
    elif pilihan=="c":
        idx = 2
    elif pilihan=="d":
        idx = 3
    elif pilihan=="e":
        idx = 4
    else:
        idx = 5
        print("---------------------KODE SALAH---------------------")
        print("              Masukan Kode Yang Sesuai              ")
        break 

    print(" Nama Merk Oli Motor = " + OliMotor[idx])
    print(" Harga Oli Motor 1L = Rp " + str(harga[idx])) 


    jumlahbeli=int(input(" Masukan jumlah Oli Motor yang dibeli = " ))  

    harga = harga[idx]
    totalharga = harga * jumlahbeli

    print(" Total Harga     = Rp " + str(totalharga))

    if totalharga > 200000: 
        setelahdiskon =totalharga-5/100*totalharga   
        print("diskon 5% jika pembelian minimum 200rb = Rp " , str(setelahdiskon))
    
    
        HargasesudahPPN = totalharga*PPN+setelahdiskon

        print(" total harga dikenakan Pajak PPN 1% = Rp " + str(HargasesudahPPN))

        ulang=input(" ulang program? Y/T = ")
        if ulang=="t" or ulang=="T":
            break