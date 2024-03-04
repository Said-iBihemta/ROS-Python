#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 09:48:54 2024
Publisher-Subscriber Uygulaması: Abone Düğümü
@author: bekirsaid
"""

import rospy
from ogretici_paket.msg import BataryaDurum

def bataryaFonksiyonu(mesaj):
    rospy.loginfo("Robot şarjı: %s"%mesaj.batarya)
    
def mesajDİnle():
    rospy.init_node("abone_dugumu")
    rospy.Subscriber("batarya_konusu",BataryaDurum,bataryaFonksiyonu)
    rospy.spin()    

mesajDİnle()