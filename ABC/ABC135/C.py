from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans = 0
for i in range(N):
    if A[i] >= B[i]:
        ans += B[i]
    else:
        ans += A[i]
        rest = B[i] - A[i]
        A[i] = 0
        if A[i+1] >= rest:
            ans += rest
            A[i+1] -= rest
        else:
            ans += A[i+1]
            A[i+1] = 0
print(ans)

        