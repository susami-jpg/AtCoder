from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

N = int(input())
ans = 0
if N >= 1000:
    ans += N - 999
if N >= 1000000:
    ans += N - 999999
if N >= 1000000000:
    ans += N - 999999999
if N >= 1000000000000:
    ans += N - 999999999999
if N >= 1000000000000000:
    ans += N - 999999999999999
print(ans)
