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
mx = 10**6 + 1
pow_2 = [1] * mx
for i in range(1, mx):
    pow_2[i] = pow_2[i-1] * 2
    pow_2[i] %= MOD
acc_pow_2 = [1] * mx
acc_pow_2
for i in range(1, mx):
    acc_pow_2[i] = acc_pow_2[i-1] + pow_2[i]
    acc_pow_2[i] %= MOD
    
N, D = map(int, input().split())
ans = 0
if N-D-1 >= 0:
    ans += acc_pow_2[N-D-1] * pow_2[D]
    ans %= MOD
for k in range(1, D):
    if k > D-k:break
    if k == D-k:
        prod = 1
    else:
        prod = 2
    md = max(k, D-k)
    if N-md-1 < 0:continue
    ans += acc_pow_2[N-md-1] * pow_2[k-1] * pow_2[D-k-1] * prod
    ans %= MOD
print((ans*2)%MOD)


