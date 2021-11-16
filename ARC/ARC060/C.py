from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

N, A = map(int, input().split())
x = list(map(int, input().split()))
max_n = A*N + 1
#dp[i][j][k]:= i番目までのカードからk枚を使ってj和をjにするような場合の数
dp = [[[0] * (N+1) for _ in range(max_n)] for _ in range(N+1)]
dp[0][0][0] = 1
for i in range(N):
    for j in range(max_n):
        for k in range(N+1):
            dp[i+1][j][k] += dp[i][j][k]
            if j+x[i] < max_n and k+1 <= N:
                dp[i+1][j+x[i]][k+1] += dp[i][j][k]

ans = 0
for k in range(1, N+1):
    ans += dp[N][A*k][k]
print(ans)
