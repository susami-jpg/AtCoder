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
S = input()
dp = [[0] * (N+1) for _ in range(N+1)]
for i in range(N-1, -1, -1):
    for j in range(N-1, -1, -1):
        if S[i] != S[j]:
            dp[i][j] = 0
        else:
            dp[i][j] = dp[i+1][j+1] + 1

ans = 0
for i in range(N-1):
    for j in range(i+1, N):
        lim = min(j-i, dp[i][j])
        ans = max(ans, lim)
print(ans)

