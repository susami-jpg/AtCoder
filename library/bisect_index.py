# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 16:18:31 2021

@author: kazuk
"""

from bisect import bisect_left, bisect_right

def LessThan(K: int, A: list) -> int:
    "配列Aの中のうち、k未満の個数と終わりの0indexを返すライブラリ"
    "-1の時は解が無い時"
    ans = bisect_left(A, K)
    return ans, (-1 if ans == 0 else ans - 1)

"""
a = [10, 10, 10, 11, 11, 12, 12, 12, 12, 14, 16, 12, 18, 10, 12]
a.sort()
print(a)
num, ind = LessThan(12, a) # 個数, 終わりの0index
print(num, ind)
[10, 10, 10, 10, 11, 11, 12, 12, 12, 12, 12, 12, 14, 16, 18]
6 5
"""


def More(K: int, A: list) -> int:
    "配列Aの中のうち、kより大きいものの個数と始まりの0indexを返すライブラリ"
    "-1の時は解が無い時"
    ans = bisect_right(A, K)
    l = len(A)
    return l - ans, (ans if ans <= l - 1 else -1)

"""
a = [10, 10, 10, 11, 11, 12, 12, 12, 12, 14, 16, 12, 18, 10, 12]
a.sort()
print(a)
num, ind = More(12, a) # 個数, 始まりの0index
print(num, ind)
[10, 10, 10, 10, 11, 11, 12, 12, 12, 12, 12, 12, 14, 16, 18]
3 12
"""


def OrLessThan(K: int, A: list) -> int:
    "配列Aの中のうち、k以下の個数と終わりの0indexを返すライブラリ"
    "-1の時は解が無い時"
    ans = bisect_right(A, K)
    return ans, (-1 if ans == 0 else ans - 1)

"""
a = [10, 10, 10, 11, 11, 12, 12, 12, 12, 14, 16, 12, 18, 10, 12]
a.sort()
print(a)
num, ind = OrLessThan(12, a) # 個数, 終わりの0index
print(num, ind)
[10, 10, 10, 10, 11, 11, 12, 12, 12, 12, 12, 12, 14, 16, 18]
12 11
"""


def OrMore(K: int, A: list) -> int:
    "配列Aの中のうち、k以上の個数と始まりの0indexを返すライブラリ"
    "-1の時は解が無い時"
    ans = bisect_left(A, K)
    l = len(A)
    return l - ans, (ans if ans <= l - 1 else -1)

"""
a = [10, 10, 10, 11, 11, 12, 12, 12, 12, 14, 16, 12, 18, 10, 12]
a.sort()
print(a)
num, ind = OrMore(12, a) # 個数, 始まりの0index
print(num, ind)
[10, 10, 10, 10, 11, 11, 12, 12, 12, 12, 12, 12, 14, 16, 18]
9 6
"""