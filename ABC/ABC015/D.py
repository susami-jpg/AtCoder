from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

W = int(input())
N, K = map(int, input().split())
pictures = [tuple(map(int, input().split())) for _ in range(N)]
dp_prev = [[0] * (W+1) for _ in range(K+1)]
dp = [[0] * (W+1) for _ in range(K+1)]

for i in range(N):
    a, b = pictures[i]
    for j in range(K+1):
        for k in range(W+1):
            dp[j][k] = max(dp_prev[j][k], dp[j][k])
            if j+1 <= K and k+a <= W:
                dp[j+1][k+a] = max(dp[j+1][k+a], dp_prev[j][k] + b)
    dp_prev = dp
    dp = [[0] * (W+1) for _ in range(K+1)]

ans = 0
for j in range(K+1):
    for k in range(W+1):
        ans = max(ans, dp_prev[j][k])
print(ans)
