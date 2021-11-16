from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt, factorial
from copy import copy, deepcopy
INF = 10**15
MOD = 998244353

N, M, K = map(int, input().split())
ban_edge = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    ban_edge[u].append(v)
    ban_edge[v].append(u)
for v in range(N):
    ban_edge[v].append(v)
    
dp_prev = [0] * N
dp_prev[0] = 1
S_prev = 1
for _ in range(K):
    dp = [0] * N
    #print(dp_prev)
    for v in range(N):
        S = S_prev
        for ban in ban_edge[v]:
            S -= dp_prev[ban]
        dp[v] += S
        dp[v] %= MOD
    S_prev = 0
    for v in range(N):
        S_prev += dp[v]
        S_prev %= MOD
    dp_prev = dp
#print(dp_prev)

ans = dp_prev[0]
print(ans%MOD)
