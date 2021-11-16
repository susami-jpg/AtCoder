from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
INF = 10**15
MOD = 10**9+7

S, T = input().split()
a = [S, T]
a.sort()
if a[0] == S:
    print('Yes')
else:
    print('No')
    