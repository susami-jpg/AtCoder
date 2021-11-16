from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

W, H, x, y = map(int, input().split())
ans = (W*H)/2
if W == 2*x and H == 2*y:
    print(ans, 1)
else:
    print(ans, 0)
    