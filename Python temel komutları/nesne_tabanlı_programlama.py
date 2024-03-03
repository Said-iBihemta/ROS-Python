#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 00:55:55 2024
Nesne tabanlı programalma
@author: bekirsaid
"""
class   Sensor:
    def __init__(self, isim,tip,fiyat):
        self.s_ismi = isim
        self.s_tip = tip
        self.s_fiyat = fiyat  
        
    def bilgi_yazdır(self):
        print("İsim: {}, tip: {}, fiyat: {}".format(self.s_ismi,self.s_tip,self.s_fiyat))
   
    def fiyat_güncelle(self,yeni_fiyat):
        self.s_fiyat = yeni_fiyat
        return self.s_fiyat
nesne1 = Sensor("a","mesafe",300)
nesne1.fiyat_güncelle(800)
nesne1.bilgi_yazdır()
print(dir(Sensor))

#print(nesne1.s_fiyat)
nesne2 = Sensor("b","kamera",500)
#print(nesne2.s_fiyat)

#s1_isim = "a"
#s1_tip = "mesafe"
#s1_fiyat = 300
#
#
#s2_isim = "b"
#s2_tip = "kamera"
#s2_fiyat = 500
#
#s3_isim = "c"
#s3_tip = "konum"
#s3_fiyat = 200