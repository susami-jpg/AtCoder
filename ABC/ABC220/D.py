from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 998244353

N = int(input())
A = list(map(int, input().split()))
dp = [[0] * 10 for _ in range(N)]
dp[0][A[0]] = 1
for i in range(N-1):
    for j in range(10):
        nxtj = (j+A[i+1])%10
        dp[i+1][nxtj] += dp[i][j]
        dp[i+1][nxtj] %= MOD

        nxtj = (j*A[i+1])%10
        dp[i+1][nxtj] += dp[i][j]
        dp[i+1][nxtj] %= MOD

for j in range(10):
    print(dp[-1][j]%MOD)

