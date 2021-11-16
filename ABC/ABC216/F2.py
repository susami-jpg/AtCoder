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
ab_set = []
for i in range(N):
    ab_set.append((A[i], B[i]))
ab_set.sort()

dp  = [[0] * 5001 for _ in range(N+1)]
dp[0][0] = 1
ans = 0
for i in range(N):
    a, b = ab_set[i]
    acc_S = 0
    for j in range(5001):
        if dp[i][j]:
            dp[i+1][j] += dp[i][j]
            dp[i+1][j] %= MOD
            if j+b <= 5000:
                dp[i+1][j+b] += dp[i][j]
                dp[i+1][j+b] %= MOD
                if j+b <= a:
                    acc_S += dp[i][j]
                    acc_S %= MOD
    #print(acc_S)
    ans += acc_S%MOD
    ans %= MOD
#for row in dp:
    #print(row[:10])
print(ans)

