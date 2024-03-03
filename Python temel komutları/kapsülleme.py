#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 01:19:53 2024
Kapsülleme
@author: bekirsaid
"""

class   Sensor:
    def __init__(self, isim,tip,fiyat):
        self.s_ismi = isim
        self.s_tip = tip
        self.__s_fiyat = fiyat  
        
    def bilgi_yazdır(self):
        print("İsim: {}, tip: {}, fiyat: {}".format(self.s_ismi,self.s_tip,self.s_fiyat))
   
    def fiyat_göster(self):
        return self.__s_fiyat
    
nesne = Sensor("a","mesafe",300)
print(nesne.fiyat_göster())
#    nesne.bilgi_yazdır()
#    print(dir(Sensor))

#İlk olarak class kısmında self.s_fiyat kısmında 's' harifnin başına
#iki adet alt çizgi (__) ekledik. Ve fİyat özelliğini private'ledik
#daha sonra  def fiyat_göster(self): tanımalmasını yaptık ve ardından
#return( self.__s_fiyat)
#kodunu yazarak kapsüllemeyi bozduk.