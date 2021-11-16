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
rel = []
for _ in range(M):
    a, b = map(int, input().split())
    rel.append((b, a))
rel.sort()
ans = 0
right = -INF
for i in range(M):
    r, l = rel[i]
    if right <= l:
        ans += 1
        right = r
print(ans)
