from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
INF = 10**15
MOD = 10**9+7

N, M = map(int, input().split())
rec = defaultdict(int)
graph = defaultdict(int)
for _ in range(M):
    a, b = map(int, input().split())
    if a == b:continue
    f = max(a, b)
    t = min(a, b)
    if graph[(f, t)]:continue
    rec[f] += 1
    graph[(f, t)] += 1

ans = 0
for v in range(1, N+1):
    if rec[v] == 1:
        ans += 1
print(ans)