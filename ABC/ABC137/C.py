from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

rec = defaultdict(int)
N = int(input())
for _ in range(N):
    s = input()
    d = [0] * 26
    for i in range(10):
        d[ord(s[i]) - 97] += 1
    d = list(map(str, d))
    d = "".join(d)
    rec[d] += 1

rec = dict(rec)
ans = 0
for key, val in rec.items():
    ans += val*(val-1)//2
print(ans)

    
        