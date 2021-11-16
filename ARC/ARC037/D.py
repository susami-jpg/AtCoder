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
N, M = map(int, input().split())
edge = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    edge[u].append(v)
    edge[v].append(u)

def dfs(v, par=-1):
    if seen[v]:
        return False
    ok = True
    seen[v] = 1
    for nextv in edge[v]:
        if nextv == par:continue
        ok &= dfs(nextv, v)
    return ok

seen = [0] * N
ans = 0
for v in range(N):
    if seen[v]:continue
    if dfs(v):
        ans += 1
print(ans)
