from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
INF = 10**15
MOD = 10**9+7

N, K = map(int, input().split())
sw = [tuple(map(int, input().split())) for _ in range(N)]

def is_ok(x):
    cnd = []
    for w, p in sw:
        cnd.append(w*(p-x))
    cnd.sort(reverse=True)
    if sum(cnd[:K]) >= 0:
        return True
    else:
        return False


ok = 0
ng = 100
for _ in range(100):
    mid = (ok + ng) / 2
    if is_ok(mid):
        ok = mid
    else:
        ng = mid

print(ok)
