from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt, factorial
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

N = int(input())
ans = 0
range_set = [tuple(map(int, input().split())) for _ in range(N)]
for i in range(N-1):
    for j in range(i+1, N):
        t1, l1, r1 = range_set[i]
        t2, l2, r2 = range_set[j]
        l1 *= 2
        r1 *= 2
        l2 *= 2
        r2 *= 2
        if t1 == 2:
            r1 -= 1
        elif t1 == 3:
            l1 += 1
        elif t1 == 4:
            l1 += 1
            r1 -= 1
        if t2 == 2:
            r2 -= 1
        elif t2 == 3:
            l2 += 1
        elif t2 == 4:
            l2 += 1
            r2 -= 1
            
        #包含パターン
        if max(l1, l2) <= min(r1, r2):
            ans += 1
print(ans)
