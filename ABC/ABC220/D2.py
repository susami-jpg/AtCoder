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

N = int(input())
A = list(map(int, input().split()))
dp = [[0] * 10 for _ in range(N)]
dp[0][A[0]] = 1
for i in range(N-1):
    for j in range(10):
        if dp[i][j] == 0:continue
        nxt = A[i+1]
        dp[i+1][(j+nxt)%10] += dp[i][j]
        dp[i+1][(j+nxt)%10] %= MOD
        dp[i+1][(j*nxt)%10] += dp[i][j]
        dp[i+1][(j*nxt)%10] %= MOD

for j in range(10):
    print(dp[N-1][j])
    
