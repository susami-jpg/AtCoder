from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 998244353

N, D = map(int, input().split())
#dp[i]:= 0indexで頂点0を0段目としたときにi段目にある頂点数
dp = [0] * N
for i in range(N):
    dp[i] = pow(2, i, MOD)

#acc_dp[i]:= 0indexで頂点0を0段目としたときにi段目より上にある頂点数
acc_dp = list(accumulate(dp))

ans = 0

#頂点vを始点としてD個下へ向かう場合
if D < N:
    ans += acc_dp[N-1-D] * dp[D] * 2
    ans %= MOD

#頂点vを折り返し地点とする場合
for k in range(1, D//2+1):
    if 0 <= N-1-D+k < N and D-k-1 < N:
        if k == D-k:
            prod = 1
        else:
            prod = 2
        prod *= acc_dp[N-1-D+k] 
        prod %= MOD
        prod *= dp[k-1] 
        prod %= MOD
        prod *= dp[D-k-1] * 2
        ans += prod
        ans %= MOD
print(ans)




            




