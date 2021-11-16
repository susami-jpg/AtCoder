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
N, M = map(int, input().split())
edge = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append(b)

def dfs(v):
    global cnt
    seen[v] = 1
    cnt += 1
    for nextv in edge[v]:
        if seen[nextv]:continue
        dfs(nextv)
    return

ans = 0
for v in range(N):
    seen = [0] * N
    cnt = 0
    dfs(v)
    ans += cnt
print(ans)
