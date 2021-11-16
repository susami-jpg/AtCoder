from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

rec = defaultdict(int)
N, M = map(int, input().split())
A = list(map(int, input().split()))
for a in A:
    rec[a] += 1

for _ in range(M):
    b, c = map(int, input().split())
    rec[c] += b

cnt = N
ans = 0

for (key, val) in sorted(dict(rec).items(), reverse=True):
    if cnt-val < 0:
        ans += cnt*key
        break
    else:
        ans += val*key
        cnt -= val
print(ans)