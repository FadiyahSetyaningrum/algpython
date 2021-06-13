ulang = "y"
while ulang=="y" or ulang=="Y":

    hargaprinter=660000 
    print ("=================================")
    print ("  Nilai Total Pembelian Printer  ")
    print ("=================================")

    jmlbeli = input(">> Jumlah Printer Epson T20 yang dibeli = ")

    total = int(hargaprinter)*int(jmlbeli)

    print("Total Pembelian Printer Epson T20 = Rp " + str(total))

    ulang=input(">>ulang program? Y/T = ")
    if ulang=="t" or ulang=="T":
        break