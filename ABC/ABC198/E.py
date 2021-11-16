from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

setrecursionlimit(10**7)
N = int(input())
C = list(map(int, input().split()))
edge = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append(b)
    edge[b].append(a)

ans = []
def dfs(v, seen, par = -1):
    global ans
    if seen[C[v]] == 0:
        ans.append(v+1)
    seen[C[v]] += 1
    for nextv in edge[v]:
        if nextv == par:continue
        dfs(nextv, seen, v)
    seen[C[v]] -= 1
    return

dfs(0, [0] * (10**5+1))
ans.sort()
print(*ans)
