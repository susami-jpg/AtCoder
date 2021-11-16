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
rel = [[0] * N for _ in range(N)]
for _ in range(M):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    rel[x][y] = 1

ans = 0
for i in range(1 << N):
    group = []
    for j in range(N):
        if (i>>j)&1:
            group.append(j)
    L = len(group)
    ok = True
    for a in range(L-1):
        for b in range(a+1, L):
            if rel[group[a]][group[b]] == 0:
                ok = False
        
    if ok:
        ans = max(ans, L)
print(ans)

