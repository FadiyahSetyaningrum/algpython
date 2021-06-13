ulang = "y"
while ulang=="y" or ulang=="Y":

    print ("=================================")
    print ("  Nilai Total Pembelian Printer  ")
    print ("=================================")

    jmlbeli = int(input('Jumlah Printer Epson T20 yang dibeli : '))
    hargaprinter=660000
    disc = 0.15
    total = hargaprinter * jmlbeli 

    if total >= 1500000 : disc = 0.15

    print("Harga sebelum diskon                 = Rp. ",total)
    print("Diskon printer                       =",disc)
    print("Total Pembelian Printer Epson T20    = Rp. ",str(total-disc))

    ulang=input(">>ulang program? Y/T = ")
    if ulang=="t" or ulang=="T":
        break