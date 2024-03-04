#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 09:38:32 2024
Publisher- Subscriber Uygulaması: Yayıncı Düğümü 
@author: bekirsaid
"""
import rospy
from ogretici_paket.msg import BataryaDurum

def mesajYayinla():
    rospy.init_node("yayinci_dugumu",anonymous = True)
    pub = rospy.Publisher("batarya_konusu",BataryaDurum,queue_size=10)
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        durum = "%25"
        rospy.loginfo(durum)
        pub.publish(durum)
        rate.sleep()
        
        
mesajYayinla()
