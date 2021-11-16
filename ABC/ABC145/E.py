from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

N, T = map(int, input().split())
dishes = [(0, 0)] + [tuple(map(int, input().split())) for _ in range(N)]
dishes.sort()

#dp[i][j]:= i番目までの料理を見て、Aの和がj以下である時のおいしさの最大値
dp = [[0] * T for _ in range(N+1)]
for i in range(1, N+1):
    a, b = dishes[i]
    for j in range(T):
        dp[i][j] = max(dp[i][j], dp[i-1][j])
        if j-1 >= 0:
            dp[i][j] = max(dp[i][j], dp[i][j-1])
        if j-a >= 0:
            dp[i][j] = max(dp[i][j], dp[i-1][j-a] + b)

ans = 0
for i in range(1, N+1):
    #i番目の料理を最後に食べる場合
    a, b = dishes[i]
    ans = max(ans, dp[i-1][T-1] + b)
print(ans)

