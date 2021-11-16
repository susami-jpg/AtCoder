from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

N, K = map(int, input().split())
A = list(int(input()) for _ in range(N))
if 0 in A:
    print(N)
    exit()
r = 0
prod = 1
ans = 0
#[l, r)
for l in range(N):
    while r < N and prod * A[r] <= K:
        prod *= A[r]
        r += 1
    ans = max(ans, r-l)
    if r == l:
        r += 1
    else:
        prod //= A[l]
print(ans)
