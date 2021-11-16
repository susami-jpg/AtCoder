from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

N = list(map(int, list(input())))
n = len(N)
ans = 0
for i in range(1<<n):
    cnd1 = []
    cnd2 = []
    for j in range(n):
        if (i>>j)&1:
            cnd1.append(N[j])
        else:
            cnd2.append(N[j])
    cnd1.sort(reverse=True)
    cnd2.sort(reverse=True)
    cnd1 = list(map(str, cnd1))
    cnd2 = list(map(str, cnd2))
    if not cnd1 or not cnd2:continue
    if cnd1[0] == 0 or cnd2[0] == 0:continue
    c1 = int(''.join(cnd1))
    c2 = int(''.join(cnd2))
    if c1 == 0 or c2 == 0:continue
    ans = max(ans, c1*c2)
print(ans)

