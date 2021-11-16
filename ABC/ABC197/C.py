from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import acos, sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

N = int(input())
A = list(map(int, input().split()))

ans = INF
for i in range(1<<(N-1)):
    now_or = A[0]
    cnd = []
    for j in range(N-1):
        if (i>>j)&1:
            cnd.append(now_or)
            now_or = A[j+1]
        else:
            now_or |= A[j+1]
    cnd.append(now_or)
    xor = cnd[0]
    L = len(cnd)
    for j in range(1, L):
        xor ^= cnd[j]
    ans = min(ans, xor)

print(ans)
