from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

N, M = map(int, input().split())
dp = [0] * (N+1)
dp[0] = 1
out = [0] * (N+1)
for _ in range(M):
    a = int(input())
    out[a] = 1

for i in range(N+1):
    if out[i]:continue
    if i-1 >= 0:
        dp[i] += dp[i-1]
    if i-2 >= 0:
        dp[i]  += dp[i-2]
    dp[i] %= MOD

print(dp[N]%MOD)



