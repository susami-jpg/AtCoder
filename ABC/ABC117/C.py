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
X = list(map(int, input().split()))

if N >= M:
    print(0)
    exit()
X.sort()
edge = []
for i in range(1, M):
    edge.append(X[i]-X[i-1])

edge.sort(reverse=True)
ans = sum(edge) - sum(edge[:N-1])
print(ans)

