from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt, factorial
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

N, M, L, X = map(int, input().split())
A = list(map(int, input().split()))

#dp[i][j]:= i番目までのaからいくつか選択して休息所jに行く最小の周回数   
dp = [[INF] * M for _ in range(N+1)]
dp[0][0] = 1
for i in range(N):
    for j in range(M):
        if dp[i][j] == INF:continue
        dp[i+1][j] = min(dp[i+1][j], dp[i][j])
        if j+A[i] >= M:
            dp[i+1][(j+A[i])%M] = min(dp[i+1][(j+A[i])%M], dp[i][j] + (j+A[i])//M)
        else:
            dp[i+1][j+A[i]] = min(dp[i+1][j+A[i]], dp[i][j])
            
if dp[N][L] > X:
    print("No")
else:
    print("Yes")