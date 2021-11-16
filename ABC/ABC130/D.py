from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

N, K = map(int, input().split())
A = list(map(int, input().split()))

r = -1
S = 0
ans = 0
for l in range(N):
    while r+1 < N and S+A[r+1] < K:
        S += A[r+1]
        r += 1
    ans += N-1-r
    S -= A[l]
print(ans)
