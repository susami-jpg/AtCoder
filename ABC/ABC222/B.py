from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

N, P = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
for i in range(N):
    if A[i] < P:
        ans += 1

print(ans)
