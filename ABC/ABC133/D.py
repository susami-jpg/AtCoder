from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

N = int(input())
A = list(map(int, input().split()))
S = sum(A)//2
not_X1 = 0
for i in range(1, N, 2):
    not_X1 += A[i]
X1 = S-not_X1
ans = [0] * N
ans[0] = X1
for i in range(1, N):
    ans[i] = (A[i-1]-ans[i-1])
ans = list(map(lambda x: x*2, ans))
print(*ans)
    

    