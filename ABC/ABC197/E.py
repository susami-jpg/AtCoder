from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

N = int(input())
boal = [[] for _ in range(N+1)]
is_boal = set()
for _ in range(N):
    x, c = map(int, input().split())
    boal[c].append(x)
    is_boal.add(c)

place = [[0] * 2 for _ in range(N+1)]
for i in range(1, N+1):
    if boal[i]:
        place[i][0] = min(boal[i])
        place[i][1] = max(boal[i])
    else:
        place[i][0] = place[i-1][0]
        place[i][1] = place[i-1][1]
dp = [[INF] * 2 for _ in range(N+1)]

dp[0][0] = dp[0][1] = 0

for i in range(1, N+1):
    prevl, prevr = place[i-1]
    l, r = place[i]
    if i in is_boal:
        dp[i][0] = min(dp[i-1][0] + abs(prevl-r), dp[i-1][1] + abs(prevr-r)) + abs(r-l)
        dp[i][1] = min(dp[i-1][0] + abs(prevl-l), dp[i-1][1] + abs(prevr-l)) + abs(r-l)
    else:
        dp[i][0] = dp[i-1][0]
        dp[i][1] = dp[i-1][1]
print(min(dp[N][0] + abs(place[N][0]), dp[N][1] + abs(place[N][1])))

    