from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
INF = 10**15
MOD = 10**9+7

N, K = map(int, input().split())
p = list(map(int, input().split()))

E = [0] * 1001
for i in range(1, 1001):
    E[i] += E[i-1] + i

ans = 0
for i in range(K):
    ans += E[p[i]]/p[i]
cnd = ans
for i in range(K, N):
    cnd += E[p[i]]/p[i]
    cnd -= E[p[i-K]]/p[i-K]
    ans = max(ans, cnd)
print(ans)
