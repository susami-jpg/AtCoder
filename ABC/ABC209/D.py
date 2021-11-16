from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt, factorial
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

setrecursionlimit(10**7)
N, Q = map(int, input().split())
edge = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    edge[a-1].append(b-1)
    edge[b-1].append(a-1)

color = [-1] * N
def dfs(v, c, par=-1):
    color[v] = c
    for nextv in edge[v]:
        if nextv == par:continue
        dfs(nextv, 1-c, v)
    return

dfs(0, 0)
for _ in range(Q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if color[c] == color[d]:
        print("Town")
    else:
        print("Road")
        
