# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 20:56:51 2021

@author: ASUS
"""

print("===========================================")

total1=0
jenis1=""
porsi=0
gelas=0

def fungsimakanan():
   global total1
   global porsi
   global jenis1
   print("Menu Makanan")
   print("===========================================")
   print(" a. Nasi Goreng          15.000")
   print(" b. Lontong Goreng       14.900")
   print(" c. Bakso Goreng         12.900")
   print(" d. Rujak Goreng         13.000")
   print(" e. Rujak Bakso          15.000")
   print(" f. Rujak Bakso Pecel    17.000")
   nomor=str(input("Masukan Pilihan: "))
   porsi= int(input("Jumlah yang dibeli: "))
   
   if nomor=="a":
       total1=porsi*15000
       print (porsi," Nasi Goreng = Rp", total1)
       jenis1=("Nasi Goreng")
   elif nomor=="b":
       total1=porsi*14900
       print (porsi," Lontong Goreng  = Rp", total1)
       jenis1=("Lontong Goreng ")
   elif nomor=="c":
       total1=porsi*12900
       print (porsi, " Bakso Goreng = Rp", total1)
       jenis1=("Bakso Goreng")
   elif nomor=="d":
       total1=porsi*13000
       print (porsi, " Rujak Goreng = Rp", total1)
       jenis1=("Rujak Goreng")
   elif nomor=="e":
       total1=porsi*15000
       print (porsi, " Rujak Bakso = Rp", total1)
       jenis1=("Rujak Bakso")
   elif nomor=="f":
       total1=porsi*17000
       print (porsi, " Rujak Bakso Pecel = Rp", total1)
       jenis1=("Rujak Bakso Pecel")
   else:
      print("Pilihan tidak ada, silahkan masukan lagi!!")
      fungsimakanan()


fungsimakanan()

total2=0
jenis2=""

def fungsiminuman():
   global total2
   global jenis2
   global gelas
   print("===========================================")
   print("Menu Minuman")
   print("===========================================")
   print(" a. Teh Dingin/Hangat/Panas      2.000")
   print(" b. Kopi Dingin                  5.000")
   print(" c. Kopi Teh Panas               6.500")
   print(" d. Coca Cola Dingin             3.500")
   print(" e. Coca Cola Panas              5.000")
   nomor=str(input("Masukan Pilihan: "))
   gelas= int(input("Jumlah yang dibeli: "))

   if nomor=="a":
       total2=gelas*2000
       print (gelas," Es Teh = Rp", total2)
       jenis2=("Es Teh")
   elif nomor=="b":
       total2=gelas*5000
       print (gelas, " Gelas Es Jeruk = Rp", total2)
       jenis2=("Es Jeruk")
   elif nomor=="c":
       total2=gelas*6500
       print (gelas, " Gelas Es Kopi = Rp", total2)
       jenis2=("Es Kopi")
   elif nomor=="d":
       total2=gelas*3500
       print (gelas, " Gelas Es Kopi = Rp", total2)
       jenis2=("Es Kopi")
   elif nomor=="e":
       total2=gelas*5000
       print (gelas, " Gelas Es Kopi = Rp", total2)
       jenis2=("Es Kopi")
   else:
      print("Pilihan tidak ada, silahkan masukan lagi!!")
      fungsiminuman()


fungsiminuman()
    
totalsemua=0
totalsemua=total1+total2
print("\nTotal harus Dibayar: Rp",totalsemua)
uang=int(input("Uang Tunai Pembeli: Rp."))
kembalian=int(uang-totalsemua)
print("Kembalian :",kembalian)

print("===============================================")
print("=============== STRUK PEMBELIAN ===============")
print("===============================================")
print (" Pembelian              :",porsi,jenis1,"-", total1)
print ("                         ",gelas,jenis2,"-", total2)
print (" Tagihan                : Rp.",totalsemua)
print (" Uang                   : Rp.",uang)
print (" Kembalian              : Rp.",kembalian)
print("===============================================")
print("===============================================")
