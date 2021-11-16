from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7
"""
N = int(input())
Y = defaultdict(set)
point = set()
for _ in range(N):
    x, y = map(int, input().split())
    Y[x].add(y)
    point.add(x)

ans = 0
point = list(point)
n = len(point)
for i in range(n-1):
    for j in range(i+1, n):
        s1 = Y[point[i]]
        s2 = Y[point[j]]
        k = len(s1&s2)
        ans += k*(k-1)//2
print(ans)
"""

N = int(input())
points = []
points_set = set()
for _ in range(N):
    x, y = map(int, input().split())
    points.append((x, y))
    points_set.add((x, y))

ans = 0
for i in range(N):
    for j in range(N):
        p1 = points[i]
        p2 = points[j]
        if p1[0] < p2[0] and p1[1] > p2[1]:
            q1 = (p1[0], p2[1])
            q2 = (p2[0], p1[1])
            if q1 in points_set and q2 in points_set:
                ans += 1

print(ans)

    
        
    
    