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
B = list(map(int, input().split()))
dp = [[0] * 3001 for _ in range(N)]
for j in range(A[0], B[0]+1):
    dp[0][j] = 1

for i in range(1, N):
    acc_prev = list(accumulate(dp[i-1]))
    for j in range(A[i], B[i]+1):
        dp[i][j] += acc_prev[j]
        dp[i][j] %= MOD

ans = 0
for j in range(3001):
    ans += dp[N-1][j]
    ans %= MOD
print(ans)
