#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Action Service-Client Uygulaması: Client Düğümü
"""

import rospy
import actionlib
from ogretici_paket.msg import GorevDurumAction, GorevDurumGoal

def bildirimFonksiyonu(bilgi):
    print("Gorev tamamlanma durumu: ", bilgi.oran)

def istekteBulun():
    rospy.init_node("action_istemci_dugumu")
    istemci = actionlib.SimpleActionClient("gorev",GorevDurumAction)
    istemci.wait_for_server()
    istek = GorevDurumGoal()
    istek.birim = 10
    istemci.send_goal(istek,feedback_cb=bildirimFonksiyonu)
    istemci.wait_for_result()
    x = istemci.get_result().sonuc
    return x

cikti = istekteBulun()
print("Gorevin son durumu: ", cikti)