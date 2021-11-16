from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

setrecursionlimit(10**7)
N = int(input())
edge = [[] for _ in range(N)]
for _ in range(N-1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    edge[u].append((v, w))
    edge[v].append((u, w))

color = [-1] * N
def dfs(v, par=-1):
    c = color[v]
    for nextv, w in edge[v]:
        if nextv == par:continue
        if w%2:
            color[nextv] = 1-c
        else:
            color[nextv] = c
        dfs(nextv, v)
    return

color[0] = 0
dfs(0)
print(*color)
