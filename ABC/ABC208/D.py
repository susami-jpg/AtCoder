from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt, factorial
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

N, M = map(int, input().split())
dp = [[INF] * N for _ in range(N)]
for i in range(N):
    dp[i][i] = 0
for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    dp[a][b] = c

ans = 0
for k in range(N):
    for i in range(N):
        for j in range(N):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
                if dp[i][j] == INF:continue
                #print(k+1, i+1, j+1, dp[i][j])
                ans += dp[i][j]

print(ans)




    
