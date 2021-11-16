from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt, factorial
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

S = list(input())
n = len(S)
cnd = []
now = S
for _ in range(n):
    cnd.append("".join(now))
    p = now.pop()
    now = [p] + now
cnd.sort()
print(cnd[0])
print(cnd[-1])

