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
MOD = 998244353
setrecursionlimit(10**7)

S = list(input())
S = list(map(int, S))[::-1]
N = len(S)
c = 1
ans = 0
for i in range(N):
    ans += S[i] * c
    ans %= MOD
    c *= 5
    c += 0.5
    c %= MOD

for i in range(N-1):
    ans *= 2
    ans %= MOD
print(int(ans))



