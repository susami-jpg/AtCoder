from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt, factorial
from decimal import Decimal
#decimalには文字列で渡す PyPyは遅いのでPython3で提出する
#d1 = Decimal('1.1') d2 = Decimal('2.3') -> d1 + d2などの演算で浮動小数点数での誤差がなくなる(割り算もok)
INF = 10**15
MOD = 10**9+7

X = input()
new_dict = dict()
for i in range(26):
    new_dict[X[i]] = chr(97+i)

def translate(s):
    new_s = []
    for i in range(len(s)):
        new_s.append(new_dict[s[i]])
    return "".join(new_s)

N = int(input())
names = []
for _ in range(N):
    s = input()
    names.append((translate(s), s))

names.sort()
for _, s in names:
    print(s)
    
