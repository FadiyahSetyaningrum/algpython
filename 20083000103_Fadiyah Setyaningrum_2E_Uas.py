# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 12:13:48 2021

@author: ASUS
"""

print("=========================================================")
print("              SLIP GAJI KARYAWAN CV.LOGOS                ")
print("=========================================================")



nama =input("Nama Karyawan                   :")
gol  =input("Golongan [1/2/3]                :")
jk   =input("Jenis kelamin                   :")
if(jk == "L" or jk == "l"):
        jk = "Laki-laki"
else:
        jk = "Perempuan"
sts  =input("Status Kawin [Kawin/Blm Kawin]  :")
if(sts == "M" or sts == "m"):
        sts = "Menikah"
else:
        sts = "Blm Menikah"

        
if gol=="1":
    gapok=2500000
    tunis=2500000*0.01
    tuna=2500000*0.02
    bruto=gapok+tuna+tunis
    biajab=bruto*0.05
    pensiunan=15500
    organisasi=3500
    gajinetto=bruto-pensiunan-organisasi
    
elif gol=="2":
    gapok=4500000
    tunis=4500000*0.03
    tuna=4500000*0.02
    bruto=gapok+tuna+tunis
    biajab=bruto*0.05
    pensiunan=15500
    organisasi=3500
    gajinetto=bruto-pensiunan-organisasi
    
elif gol=="3":
    gapok=6500000
    tunis=6500000*0.05
    tuna=6500000*0.02
    bruto=gapok+tuna+tunis
    biajab=bruto*0.05
    pensiunan=15500
    organisasi=3500
    gajinetto=bruto-pensiunan-organisasi
else:
    gol="tidak ada"
    
    

print("Gaji Pokok                      : Rp",gapok)    
print("Tunjangan Istri                 : Rp",tunis)
print("Tunajangan Anak                 : Rp",tuna)
print("Gaji Bruto                      : Rp",bruto)

print("========================================================")

print("Biaya Jabatan                   : Rp",biajab)
print("Iuran Pensiunan                 : Rp",pensiunan)
print("Iuran Organisasi                : Rp",organisasi)
print("Gaji Netto                      : Rp",gajinetto)

