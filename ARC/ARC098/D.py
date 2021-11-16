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
r = 0
ans = 0
xor = 0
S = 0
for l in range(N):
    while r < N and S + A[r] == xor^A[r]:
        S += A[r]
        xor ^= A[r]
        r += 1
    ans += r-l
    xor ^= A[l]
    S -= A[l]
print(ans)
        