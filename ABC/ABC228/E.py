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
MOD = 998244353

setrecursionlimit(10**7)
N, K, M = map(int, input().split())
def power(x, y, mod):
    if y == 0:
        return 1
    res = power(x, y//2, mod)
    res *= res
    res %= mod
    if y%2:
        res *= x
    res %= mod
    return res

if M%MOD == 0:
    exit(print(0))
else:
    print(power(M, power(K, N, MOD-1), MOD))


