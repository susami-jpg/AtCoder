from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt, factorial
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

Q = int(input())
hq = []
S = 0
for _ in range(Q):
    query = list(input())
    if len(query) > 1:
        q = int(query[0])
        x = int("".join(query[2:]))
        if q == 1:
            heappush(hq, x-S)
        else:
            S += x
    else:
        ans = heappop(hq)
        ans += S
        print(ans)
        
            