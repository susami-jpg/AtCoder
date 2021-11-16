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
A = list(map(int, input().split()))
hq = []
for a in A:
    hq.append(-a)
    
heapify(hq)
for _ in range(M):
    a = -heappop(hq)
    a //= 2
    heappush(hq, -a)
ans = -sum(hq)

print(ans)
