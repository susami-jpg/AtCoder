from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

N, M = map(int, input().split())
A = [input() for _ in range(2*N)]
points = [(0, i) for i in range(2*N)]

for j in range(M):
    points.sort(key=lambda x:(-x[0],x[1]))
    new_points = []
    for k in range(N):
        g1, p1 = points[2*k]
        g2, p2 = points[2*k+1]
        if A[p1][j] == "G":
            if A[p2][j] == "C":
                g1 += 1
            elif A[p2][j] == "P":
                g2 += 1
        elif A[p1][j] == "C":
            if A[p2][j] == "P":
                g1 += 1
            elif A[p2][j] == "G":
                g2 += 1
        else:
            if A[p2][j] == "G":
                g1 += 1
            elif A[p2][j] == "C":
                g2 += 1
        new_points.append((g1, p1))
        new_points.append((g2, p2))
    points = new_points

points.sort(key=lambda x:(-x[0],x[1]))
for _, i in points:
    print(i+1)
    