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
edge = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append(b)
    edge[b].append(a)

dist = [INF] * N
dp = [0] * N
deq = deque()
deq.append(0)
dist[0] = 0
dp[0] = 1
while deq:
    v = deq.popleft()
    for nextv in edge[v]:
        if dist[nextv] > dist[v] + 1:
            dist[nextv] = dist[v] + 1
            dp[nextv] += dp[v]
            dp[nextv] %= MOD
            deq.append(nextv)
        elif dist[nextv] == dist[v] + 1:
            dp[nextv] += dp[v]
            dp[nextv] %= MOD
        
if dist[N-1] == INF:
    print(0)
else:
    print(dp[N-1])


