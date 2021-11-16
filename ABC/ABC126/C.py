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

ans = 0
if N-K >= 0:
    ans += N-K+1
for k in range(1, min(N+1, K)):
    i = 0
    while k * pow(2, i) < K:
        i += 1
    ans += pow(0.5, i)
print(ans/N)
