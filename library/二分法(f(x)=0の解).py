# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 23:52:03 2021

@author: kazuk
"""

#scipyは使える(python3)
#f(x)=0を求めるのにほかにnewton法もある
from scipy import optimize

def f(x):
    return x**2 - 2

print(optimize.bisect(f, 0, 2))


def f(x):
    return x**2 - 2

"""
区間[a,b]を2つに分け、その中点をcとする。
f(a)*f(c)が負であれば、区間[a,c]の中にx軸との交点があるはず。
f(a)*f(c)が正であれば、区間[c,b]の中にx軸との交点があるはず。
というのを繰り返す。
"""

def bisect(f,a,b):
    #少数第何位までの誤差をゆるすか
    eps = 0.000001
    #print("n\tc\tf(c)")
    n = 1
    while True:
        c = (a + b)/2
        #print("{}\t{:.5f}\t{:.5f}".format(n, c, f(c)))
        if f(a)*f(c) < 0:
            b = c
        else:
            a = c
        n += 1
        if abs(f(c)) < eps: # or abs(a - b) < eps
            break
    
    return c

a = 0
b = 5
bisect(f,a,b)