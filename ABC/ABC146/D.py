from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

setrecursionlimit(10**7)
N = int(input())
color = defaultdict(int)
G = [[] for _ in range(N)]
edge = []
for _ in range(N-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)
    edge.append((a, b))

seen = [0] * N
def dfs(v, par, used):
    if seen[v]:return
    seen[v] = 1
    cnd = 1
    for nextv in G[v]:
        if nextv == par:continue
        f = min(v, nextv)
        t = max(v, nextv)
        if cnd == used:
            cnd += 1
        color[(f, t)] = cnd
        dfs(nextv, v, cnd)
        cnd += 1
    return

dfs(0, -1, -1)
ans = [0] * (N-1)
K = 0
for i in range(N-1):
    ans[i] = color[edge[i]]
    K = max(K, color[edge[i]])

print(K)
for i in range(N-1):
    print(ans[i])
    
