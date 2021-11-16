from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
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

def bfs(s, g):
    dist = [INF] * N
    dp = [0] * N
    dist[s] = 0
    dp[s] = 1
    deq = deque()
    deq.append(s)
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
    return dp[g]

ans = bfs(0, N-1)
print(ans)

                
                