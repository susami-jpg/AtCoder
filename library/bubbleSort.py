# -*- coding: utf-8 -*-
"""
Created on Wed May 26 00:49:45 2021

@author: kazuk
"""

n = int(input())
a = list(map(int, input().split()))
cnt = 0
def bubbleSort(a, n):
    #逆の隣接要素が存在する
    flag = 1
    while flag:
        flag = 0
        for j in range(n-1, 0, -1):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]
                flag = 1
                global cnt
                cnt += 1
    return a

print(*bubbleSort(a, n))
print(cnt)
            