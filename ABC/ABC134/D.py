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
A = [0] + list(map(int, input().split()))
B = [0] * (N+1)
for i in range(N, 0, -1):
    if i > N//2:
        B[i] = A[i]
    else:
        now = i+i
        S = 0
        while now < N+1:
            S += B[now]
            now += i
        if S%2 != A[i]:
            B[i] = 1
M = 0
ans = []
for i in range(1, N+1):
    if B[i]:
        M += B[i]
        ans.append(i)
print(M)
print(*ans)