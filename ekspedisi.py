ulang = "y"
while ulang=="y" or ulang=="Y":
    print ("=============================================")
    print ("         TRANSKASI BIAYA EKSPEDISI           ")
    print ("=============================================")
    print (" Kode = A. Surabaya")
    print (" Kode = B. Bandung")
    print ("=============================================")

    kode =['a','b']

    kota = ['surabaya','bandung']
    jarak = [169,452]
    ongkirperkm = [2500,4000]
        
    pilihan = input(" Masukkan Kode Tujuan Pengiriman = ")
      
    if pilihan=="a":
        idx = 0
    elif pilihan=="b":
        idx = 1
    else:
        idx = 2
  
    print(" Pilihan Tujuan = " + kota[idx])
    print(" Jarak          = " + str(jarak[idx]) + " km")
    print(" Ongkir per km  = Rp. " + str(ongkirperkm[idx]))

    fixjarak = jarak[idx]
    fixongkirkm = ongkirperkm[idx]
    totongkir = fixjarak * fixongkirkm

    print("-------------------------------------")
    print(" Total Biaya     = Rp." + str(totongkir))

    ulang=input("ulang program? Y/T = ")
    if ulang=="t" or ulang=="T":
        break

