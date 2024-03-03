#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 13:43:42 2024
Küme Veri Yapısı  tekrar edenler tek kabul edilir
@author: bekirsaid
"""

#kume = {23,25,26,1,23,25,25}
#print(type(kume))
#print(len(kume)) 
#print(kume[1]) """ böyle bir yapı kullanıalmaz"""
#print(set("Python ile programalama"))
#kume1 = {1,2,3,4,5}
#kume2 = {1,3,5,7,9}
#kume3 = kume1 & kume2
#print(kume3)
#kume4 = kume1 | kume2
#print(kume4)
#kume5 = kume1 - kume2
#print(kume5)


""" kume metotları"""

kume1 = {1,2,3,4,5}
kume2 = {1,3,5,7,9}
print(kume1.isdisjoint(kume2))
kume3 = kume1.intersection(kume2)
print(kume3)
kume4 = kume1.union(kume2)
print(kume4)
kume5 = kume1.difference(kume2)
print(kume5)