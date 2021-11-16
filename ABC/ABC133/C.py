from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 2019

L, R = map(int, input().split())
cnd = []
for i in range(L, min(L+4040, R+1)):
    cnd.append(i%MOD)

N = len(cnd)
ans = INF
for i in range(N-1):
    for j in range(i+1, N):
        ans = min(ans, (cnd[i]*cnd[j])%MOD)
print(ans%MOD)

