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
A = list(map(int, input().split()))
rec = defaultdict(int)
r = 0
ans = 0
for l in range(N):
    while r < N and rec[A[r]] == 0:
        rec[A[r]] += 1
        r += 1
    ans = max(ans, r-l)
    rec[A[l]] -= 1
    
print(ans)
