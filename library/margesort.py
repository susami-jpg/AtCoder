# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 23:59:35 2021

@author: kazuk
"""

def sort(A):
    if len(A) < 2:
        return A
    c = len(A) // 2
    return marge(sort(A[:c]), sort(A[c:]))
#sort関数は受け取ったリストを二分し、marge関数を呼び出して整序する。margeに引き渡す引数をさらにsort関数に入れて再帰させることで最小要素つまりlen(A) = 1になるまで分解。

def marge(X, Y):
    if len(X) < 1:
        return Y
    if len(Y) < 1:
        return X
    if X[0] < Y[0]:
        return [X[0]] + marge(X[1:], Y)
    else:
        return [Y[0]] + marge(X, Y[1:])
#marge関数はリストXとYを受け取り、それぞれの先頭要素を比較して、小さいほうを先頭に持ってくる関数。
    
A = [7,5,4,6,3,5,3,3,9,7,1,2,3,1]
print(sort(A))