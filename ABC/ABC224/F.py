from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt, factorial
from copy import copy, deepcopy
INF = 10**15
MOD = 998244353

S = list(map(int, list(input())))[::-1]
N = len(S)
dp = [0] * (N+1)
for i in range(1, N+1):
    dp[i] = dp[i-1]*2 + pow(10, i-1, MOD)
    dp[i] %= MOD

ans = 0
for i in range(N):
    ans += ((pow(2, N-i-1, MOD) * S[i])%MOD) * (dp[i] + pow(10, i, MOD))
    #print(pow(2, N-i-1, MOD), S[i], dp[i], pow(10, i))
    ans %= MOD
print(ans)
