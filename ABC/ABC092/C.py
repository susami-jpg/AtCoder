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
red = [tuple(map(int, input().split())) for _ in range(N)]
blue = [tuple(map(int, input().split())) for _ in range(N)]
blue.sort()
used = [0] * N
ans = 0
for i in range(N):
    c, d = blue[i]
    max_y = -1
    cnd = None
    for j in range(N):
        a, b = red[j]
        if (not used[j]) and a < c and max_y < b < d:
            max_y = b
            cnd = j
    if cnd != None:
        ans += 1
        used[cnd] = 1
print(ans)


    