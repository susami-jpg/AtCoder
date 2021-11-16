from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
INF = 10**15
MOD = 10**9+7

N, K = map(int, input().split())
dim = [[0] * 5001 for _ in range(5001)]
for _ in range(N):
    A, B = map(int, input().split())
    dim[A][B] += 1

for i in range(5001):
    for j in range(5000):
        dim[i][j+1] += dim[i][j]

for i in range(5000):
    for j in range(5001):
        dim[i+1][j] += dim[i][j]

ans = 0
for a in range(1, 5001-K):
    for b in range(1, 5001-K):
        cnd = dim[a+K][b+K] - dim[a+K][b-1] - dim[a-1][b+K] + dim[a-1][b-1]
        ans = max(ans, cnd)
print(ans)


