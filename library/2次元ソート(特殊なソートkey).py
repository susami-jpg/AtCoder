# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 00:51:43 2021

@author: kazuk
"""

#lambda x:(-x[0],x[1]) による方法
#sort(key=lambda x:(-x[0],x[1]))
#以下は、2次元配列の 第1要素で昇順 & 第2要素で降順 sort します。
a = [(0, 1), (9, 2), (7, 3), (6, 5), (3, 5), (0, 9)]
a.sort(key=lambda x:(x[0],-x[1]))
print(a)


#2次元配列を二番目の要素に注目して降順にソートする
li = [[1,4,3],[2,3,4],[3,4,5],[4,5,6],[2,3,4],[1,5,3],[2,3,4],[5,6,7]]
li = sorted(li, reverse=True, key=lambda x: x[1])  #[1]に注目してソート
print(li)
