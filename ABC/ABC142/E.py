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
key = []
open = defaultdict(list)
for i in range(M):
    a, b = map(int, input().split())
    key.append((a, b))
    open[i] = list(map(int, input().split()))

dp = [[INF] * (1<<N) for _ in range(M+1)]
dp[0][0] = 0
for i in range(M):
    C = 0
    for c in open[i]:
        C |= (1<<(c-1))
    for S in range(1<<N):
        if dp[i][S] == INF:continue
        dp[i+1][S] = min(dp[i][S], dp[i+1][S])
        dp[i+1][S|C] = min(dp[i+1][S|C], dp[i][S] + key[i][0])

if dp[M][(1<<N)-1] == INF:
    print(-1)
else:
    print(dp[M][(1<<N)-1])

    
    