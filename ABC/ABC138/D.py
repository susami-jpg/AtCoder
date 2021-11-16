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
N, Q = map(int, input().split())
edge = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append(b)
    edge[b].append(a)

counter = [0] * N
for _ in range(Q):
    p, x = map(int, input().split())
    p -= 1
    counter[p] += x

def dfs(v, par=-1):
    if par != -1:
        counter[v] += counter[par]
    for nextv in edge[v]:
        if par == nextv:continue
        dfs(nextv, v)
    return
dfs(0)
print(*counter)

