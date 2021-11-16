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
N, K = map(int, input().split())
edge = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append(b)
    edge[b].append(a)

cnd = [-1] * N
cnd[0] = K
def dfs(v, par=-1):
    if par == -1:
        c = K-1
    else:
        c = K-2
    for nextv in edge[v]:
        if nextv == par:continue
        cnd[nextv] = c
        dfs(nextv, v)
        c -= 1
    return

dfs(0)
ans = 1
for i in range(N):
    ans *= cnd[i]
    ans %= MOD
print(ans)


        