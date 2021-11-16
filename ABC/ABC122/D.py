from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

N = int(input())
dp = [[[[0] * 4 for _ in range(4)] for _ in range(4)] for _ in range(N)]
for j in range(4):
    for k in range(4):
        for l in range(4):
            if (j, k, l) in [(0, 3, 2), (0, 2, 3), (2, 0, 3)]:continue
            dp[2][j][k][l] = 1

for i in range(2, N-1):
    for j in range(4):
        for k in range(4):
            for l in range(4):
                for m in range(4):
                    if (j, k, m) == (0, 2, 3):continue
                    if (k, l, m) in [(0, 3, 2), (0, 2, 3), (2, 0, 3)]:continue
                    if (j, l, m) == (0, 2, 3):continue
                    dp[i+1][k][l][m] += dp[i][j][k][l]
                    dp[i+1][k][l][m] %= MOD

ans = 0
for j in range(4):
    for k in range(4):
        for l in range(4):
            ans += dp[-1][k][j][l]
            ans %= MOD

print(ans)
