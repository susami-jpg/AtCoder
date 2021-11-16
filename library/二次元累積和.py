# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 13:02:02 2021

@author: kazuk
"""

#aはマップ、hは高さ、wは幅
#転置→accは遅い
def acc_d(a, h, w):
    for i in range(h):
        for j in range(w):
            if i != 0:
                a[i][j] += a[i-1][j]
    for i in range(h):
        for j in range(w):
            if j != 0:
                a[i][j] += a[i][j-1]
    return a
            

#累積和を計算したテーブルaにおいて左上の座標を(y1,x1)、右下の座標を(y2,x2)としたときの区画の累積和を返す
#0index
def kukaku(a, y1, x1, y2, x2):
    if y1 == 0 and x1 == 0:
        return a[y2][x2]
    elif y1 == 0:
        return a[y2][x2] - a[y2][x1-1]
    elif x1 == 0:
        return a[y2][x2] - a[y1-1][x2]
    else:
        return a[y2][x2] - a[y2][x1-1] - a[y1-1][x2] + a[y1-1][x1-1]
    
    