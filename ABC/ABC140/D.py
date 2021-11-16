from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

N, K = map(int, input().split())
group = []
S = input()
g = 1
for i in range(1, N):
    if S[i-1] == S[i]:
        g += 1
    else:
        group.append(g)
        g = 1
group.append(g)

if 2*K > len(group):
    group = [sum(group)]
else:
    group = [sum(group[:2*K+1])] + group[2*K+1:]


ans = 0
for g in group:
    ans += g-1
print(ans)

