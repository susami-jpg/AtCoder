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
dp = [[[0] * 101 for _ in range(101)] for _ in range(101)]
for _ in range(N):
    a, b, c, w = map(int, input().split())
    dp[a][b][c] = max(dp[a][b][c], w)

for i in range(1, 101):
    for j in range(101):
        for k in range(101):
            dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k])

for i in range(101):
    for j in range(1, 101):
        for k in range(101):
            dp[i][j][k] = max(dp[i][j][k], dp[i][j-1][k])
            
for i in range(101):
    for j in range(101):
        for k in range(1, 101):
            dp[i][j][k] = max(dp[i][j][k], dp[i][j][k-1])
            
for _ in range(M):
    x, y, z = map(int, input().split())
    print(dp[x][y][z])
    