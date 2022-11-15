# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 12:26:25 2022

@author: Yuyi
"""

from plaid_2018 import ReadPLAID_2018
import matplotlib.pyplot as plt

# =============================================================================
# 取得 個負載數據
# =============================================================================
datas, infos = ReadPLAID_2018().getSubmetered() 
size = len(datas)
label_names = []
for i in range(size):
    label = infos[i]["label"]
    if label in label_names:
        continue
    else:
        label_names.append(label)
    V, I = datas[i][0], datas[i][1]
    
    
    plt.title(label)
    plt.plot(I)
    plt.xlabel("Sample Points")
    plt.ylabel("A")
    plt.show()



# =============================================================================
#  取得聚合負載數據
# =============================================================================
datas, infos = ReadPLAID_2018().getAggregated()
for i in range(10):
    labels = infos[i]["labels"]
    name = ""
    for label in labels:
        name += label+"__"
    V, I = datas[i][0], datas[i][1]
    plt.title(name)
    plt.plot(I)
    plt.xlabel("Sample Points")
    plt.ylabel("A")
    plt.show()