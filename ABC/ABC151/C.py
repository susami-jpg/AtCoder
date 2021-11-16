from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
INF = 10**15
MOD = 10**9+7

N, M = map(int, input().split())
ac = [0] * (N+1)
wa = [0] * (N+1)
AC = 0
WA = 0
for _ in range(M):
    p, S = input().split()
    p = int(p)
    if S == "AC":
        if ac[p]:
            continue
        AC += 1
        ac[p] = 1
        WA += wa[p]
    else:
        if ac[p]:continue
        wa[p] += 1

print(AC, WA)