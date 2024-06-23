#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Service-Client Uygulaması: İstemci Düğümü
"""

import rospy
from ogretici_paket.srv import GecenZaman

def istekteBulun(x):
    rospy.wait_for_service("zaman")
    try:
        servis = rospy.ServiceProxy("zaman",GecenZaman)
        cevap = servis(x)
        return cevap.gecen_sure
    except rospy.ServiceException:
        print("Servisle alakalı hata !!!")

hedef = float(input("Hedef konum giriniz: "))
t = istekteBulun(hedef)
print("Hedefe varana kadar gecen sure: ", t)