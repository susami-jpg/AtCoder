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

N, D = map(int, input().split())
g = [0] * (N+1)
for i in range(1, N+1):
    left = i-1
    right = D-left
    g[i] = g[i-1]
    if 0 <= right <= i-1:
        prod = 1
        if left != right:
            prod = 2
        g[i] += pow(2, max(0, left-1), MOD) * pow(2, max(0, right-1), MOD) * prod
        g[i] %= MOD
    


f = [0] * (N+1)
for i in range(1, N+1):
    f[i] = f[i-1] * 2 + g[i]
    f[i] %= MOD

ans = f[N]*2
ans %= MOD
print(ans)
