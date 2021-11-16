from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

X, Y, Z, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
C.sort(reverse=True)

cnd = []
for i in range(X):
    for j in range(Y):
        cnd.append(A[i]+B[j])

hq = []
for i, c in enumerate(cnd):
    heappush(hq, (-c-C[0], i, 0))

for _ in range(K):
    ans, i, j = heappop(hq)
    print(-ans)
    if j+1 < Z:
        heappush(hq, (-cnd[i]-C[j+1], i, j+1))
