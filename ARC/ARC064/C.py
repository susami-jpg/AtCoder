from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

N, x = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
for i in range(N-1):
    diff = A[i] + A[i+1] - x
    if diff > 0:
        ans += diff
        if A[i+1] - diff >= 0:
            A[i+1] -= diff
        else:
            diff -= A[i+1]
            A[i+1] = 0
            A[i] -= diff
print(ans)
