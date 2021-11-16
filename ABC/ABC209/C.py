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
C = list(map(int, input().split()))
C.sort()
ans = C[0]
for i in range(1, N):
    ans *= (C[i] - i)
    ans %= MOD
print(ans)

    