from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt, factorial
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

setrecursionlimit(10**7)
N = int(input())
edge = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append(b)
    edge[b].append(a)

for i in range(N):
    edge[i].sort()

ans = []
def dfs(v, par=-1):
    ans.append(v+1)
    for nextv in edge[v]:
        if nextv == par:continue
        dfs(nextv, v)
        ans.append(v+1)
    return

dfs(0)
print(*ans)

