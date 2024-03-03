#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 12:46:00 2024
Koşullu Yapılar
@author: bekirsaid
"""
#hiz = 1.0

#if (hiz < 4.0):
#    print("Şart 1 sağlandı")
#if (hiz <3.0):
#    print("Şart 2 sağlandı")
#    if (hiz < 2.0):
#        print("Şart 3 sağlandı")

#if (hiz < 0.5):
#        print("Şart 1 sağlandı")
#else: (hiz > 0.5)
#print ("Şart sağlanamadı")

hiz = 0.8
if(hiz < 1.0):
    print("Şart 1 sağlandı")
elif ( hiz < 2.0):
    print("Şart 2 sağlandı")
else:
    print("2 şartta sağlanmadı")