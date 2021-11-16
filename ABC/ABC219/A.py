from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

x = int(input())
if x >= 90:
    print("expert")
elif 70 <= x < 90:
    print(90-x)
elif 40 <= x < 70:
    print(70-x)
else:
    print(40-x)
