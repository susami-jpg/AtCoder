from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7
"""
N = int(input())
box = [tuple(map(int, input().split())) for _ in range(N)]
box.sort(key=lambda x:(x[0],-x[1]))
dp = [INF] * N
for i in range(N):
    w, h = box[i]
    ind = bisect_left(dp, h)
    dp[ind] = h

ans = bisect_left(dp, INF)
print(ans)
"""
N = int(input())
box = [tuple(map(int, input().split())) for _ in range(N)]
BIT = [0] * (10**5+10)

def add(x, i):
    x += 1
    while x < 10**5+10:
        BIT[x] = max(BIT[x], i)
        x += x&-x

def get(x):
    x += 1
    S = 0
    while x > 0:
        S = max(S, BIT[x])
        x -= x&-x
    return S
        
dp = [0] * N
dp[0] = 1
box.sort(key=lambda x:(x[0],-x[1]))
for i in range(N):
    w, h = box[i]
    if i == 0:
        add(h, dp[i])
    else:
        max_n = get(h-1)
        dp[i] = max_n + 1
        add(h, dp[i])

print(max(dp))

