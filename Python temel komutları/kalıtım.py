#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 01:33:04 2024
Kalıtım
@author: bekirsaid
"""

#class Aile:
#    def __init__(self):
#        self.goz = "ela"
#        self.boy = "orta"
#        print("Göz rengi: {}, Boy uzunluğu: {}".format(self.goz,self.boy))
#        
#    def karkakteristik_ozellikler(self):
#        self.inat = False
#        self.eglenceli = True
#        print("İnatcilik: {}, Eglenceli olma: {}".format(self.inat,self.eglenceli))
#class Cocuk(Aile):
#    def __init__(self):
#        super().__init__()
#        self.goz = "Kahverengi"
#        Aile.__init__(self)
#        self.goz = "kahverengi"
#        self.boy = "uzun"
#        print("Goz rengi: {}, Boy uzunluğu: {}".format(self.goz,self.boy))
    
    
#cocuk = Cocuk()
#cocuk.karkakteristik_ozellikler()


#Çoklu kalıtım

class Anne:
    def __init__(self):
        self.goz = "ela"
        self.boy = "orta"
        print("Göz rengi: {}, Boy uzunluğu: {}".format(self.goz,self.boy))
        
    def karakteristik_ozellikler(self):
        self.inat = False
        self.eglenceli = True
        print("İnatcilik: {}, Eglenceli olma: {}".format(self.inat,self.eglenceli))
        
class Baba:
    def __init__(self):
        self.goz = "ela"
        self.boy = "uzun"
        print("Göz rengi: {}, Boy uzunluğu: {}".format(self.goz,self.boy))
        
    def karakteristik_ozellikler(self):
        self.inat = True
        self.eglenceli = False
        print("İnatcilik: {}, Eglenceli olma: {}".format(self.inat,self.eglenceli))
        
class Cocuk(Anne,Baba):
    def __init__(self):
        Baba.__init__(self)
        Baba.karakteristik_ozellikler(self)
        self.egitim = "Lisans"
        
    def egitim_goster(self):
        print("Egitim Durumu: ",self.egitim)
       
cocuk = Cocuk()
cocuk.egitim_goster()
#cocuk.karakteristik_ozellikler()