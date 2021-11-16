from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

X = list(input())
d = dict()
for ind, val in enumerate(X):
    d[val] = chr(ind+97)

name = []
N = int(input())
for _ in range(N):
    S = input()
    lS = list(S)
    nS = ""
    for s in lS:
        nS += d[s]
    name.append((nS, S))

name.sort()
for _, s in name:
    print(s)

    