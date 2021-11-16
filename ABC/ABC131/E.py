from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

N, K = map(int, input().split())

max_edge = (N-1)*(N-2)//2
if max_edge < K:
    print(-1)
    exit()

edge = []
V = [i for i in range(2, N+1)]
for v in V:
    edge.append((1, v))

rest = max_edge - K
cnt = 0
n = len(V)
for i in range(n-1):
    for j in range(i+1, n):
        if cnt == rest:
            print(len(edge))
            for u, v in edge:
                print(u, v)
            exit()
        edge.append((V[i], V[j]))
        cnt += 1
print(len(edge))
for u, v in edge:
    print(u, v)