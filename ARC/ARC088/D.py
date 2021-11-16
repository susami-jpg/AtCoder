from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

S = input()
N = len(S)
ans = N
for i in range(1, N):
    if S[i-1] != S[i]:
        ans = min(ans, max(i, N-i))
print(ans)
