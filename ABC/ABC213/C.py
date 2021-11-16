from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt, factorial
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

H, W, N = map(int, input().split())
Y = set()
X = set()
points = []
for i in range(N):
    a, b = map(int, input().split())
    points.append((i, a, b))
    Y.add(a)
    X.add(b)
Y = list(Y)
X = list(X)

Y.sort()
X.sort()
cc_Y = {}
cc_X = {}
for i in range(len(Y)):
    cc_Y[Y[i]] = i+1
for i in range(len(X)):
    cc_X[X[i]] = i+1

for i, a, b in points:
    print(cc_Y[a], cc_X[b])
     

    