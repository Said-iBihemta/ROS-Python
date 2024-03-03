#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 17:45:12 2024
Modülelr Zaman Hesaplama Modulü
@author: bekirsaid
"""
def zaman(x,v):
    t = x / v
    print("Geçen zaman: {} saniye".format(t))
    return t
    
def cevir(zaman):
    print("Geçen zaman: {}saat".format(zaman/60))

t_sn = zaman(20,1.2)
cevir(t_sn)