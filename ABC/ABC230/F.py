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

N = int(input())
A = [0] + list(map(int, input().split()))

for i in range(1, N+1):
    A[i] += A[i-1]
N += 1
dp = [0] * N
acc_dp = [0] * N
dp[0] = acc_dp[0] = 1
prev = dict()
for i in range(1, N):
    j = -1
    if A[i] in prev:
        j = prev[A[i]]
    left = 0
    if j-1 >= 0:
        left = acc_dp[j-1]
    right = acc_dp[i-1]
    dp[i] = right - left
    dp[i] %= MOD
    acc_dp[i] = acc_dp[i-1] + dp[i]
    acc_dp[i] %= MOD
    prev[A[i]] = i

ans = acc_dp[N-2]
print(ans%MOD)

    

N = int(input())
A = [0] + list(map(int, input().split()))

for i in range(1, N+1):
    A[i] += A[i-1]
N += 1
dp = [0] * N
acc_dp = [0] * N
prev = dict()
S = 1
for i in range(1, N-1):
    #全体からダメなものを引く考え方
    ban = 0
    if A[i] in prev:
        ban = prev[A[i]]
    dp[i] = S - ban
    dp[i] %= MOD
    #ダメなものは現在見ているところまでの和になるのでそれを記録しておく
    prev[A[i]] = S
    S += dp[i]
    S %= MOD
print(S%MOD)

