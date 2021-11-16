from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

N, M, P, Q, R = map(int, input().split())
chocolate = defaultdict(list)
for _ in range(R):
    x, y, z = map(int, input().split())
    x -= 1
    y -= 1
    chocolate[x].append((y, z))

ans = 0
for comb in combinations(range(N), P):
    man = [0] * M
    for woman in comb:
        for y, z in chocolate[woman]:
            man[y] += z
    man.sort(reverse=True)
    cnd = sum(man[:Q])
    ans = max(ans, cnd)
print(ans)

    
