from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt, factorial
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

N = int(input())
plots = [tuple(map(int, input().split())) for _ in range(N)]
ans = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            x1, y1 = plots[i]
            x2, y2 = plots[j]
            X, Y = plots[k]
            if Y*(x1-x2) == (y1-y2)*X + y1*(x1-x2) - x1*(y1-y2):
                continue
            ans += 1
print(ans)
