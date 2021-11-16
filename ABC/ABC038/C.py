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
ans = 0
r = 0
max_a = 0
for l in range(N):
    while r < N and max_a < A[r]:
        max_a = A[r]
        r += 1
    ans += r-l
    if l+1 == r:
        max_a = 0
print(ans)