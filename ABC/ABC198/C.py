from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

R, X, Y = map(int, input().split())
D = sqrt(X**2 + Y**2)
if D < R:
    ans = 2
elif D == R:
    ans = 1
elif D%R == 0:
    ans = D//R
else:
    ans = D//R + 1
print(int(ans))
