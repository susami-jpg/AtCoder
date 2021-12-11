from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt, factorial
from decimal import Decimal
#decimalには文字列で渡す PyPyは遅いのでPython3で提出する
#d1 = Decimal('1.1') d2 = Decimal('2.3') -> d1 + d2などの演算で浮動小数点数での誤差がなくなる(割り算もok)
INF = 10**18
MOD = 10**9+7
setrecursionlimit(10**7)

A, B = input().split()
A = list(map(int, list(A)))[::-1]
B = list(map(int, list(B)))[::-1]

na = len(A)
nb = len(B)
N = min(na, nb)
for i in range(N):
    if A[i] + B[i] >= 10:
        exit(print("Hard"))
else:
    print("Easy")
    