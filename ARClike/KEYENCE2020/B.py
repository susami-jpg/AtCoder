from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

N = int(input())
robots = []
for _ in range(N):
    x, l = map(int, input().split())
    robots.append((x+l, x-l))

robots.sort()
ans = 0
right = -INF
for i in range(N):
    r, l = robots[i]
    if right <= l:
        right = r
        ans += 1
print(ans)
