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
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append((b, c))
    edge[b].append((a, c))

D = list(map(int, input().split()))

max_val = (-1, -1)
def dfs(v, root, d=0, par=-1):
    global max_val
    stop_cost = d
    if v != root:
        stop_cost = d+D[v]
    max_val = max(max_val, (v, stop_cost))
    for nextv, c in edge[v]:
        if par == nextv:continue
        res = max(res, dfs(nextv, root, d+c, v))
    return res
    
def dfs(v, s, par=-1):
    if v == s:
        ss_cost = 0
    else:
        ss_cost = D[v]
    for nextv, c in edge[v]:
        if nextv == par:continue
        dist[nextv] = dist[v] - ss_cost + c + D[nextv]
        dfs(nextv, s, v)
    return

def dfs2(v, s, par=-1):
    if v == s:
        ss_cost = 0
    else:
        ss_cost = D[v]
    for nextv, c in edge[v]:
        if nextv == par:continue
        dist2[nextv] = dist2[v] - ss_cost + c + D[nextv]
        dfs2(nextv, s, v)
    return

def dfs3(v, s, par=-1):
    if v == s:
        ss_cost = 0
    else:
        ss_cost = D[v]
    for nextv, c in edge[v]:
        if nextv == par:continue
        dist3[nextv] = dist3[v] - ss_cost + c + D[nextv]
        dfs3(nextv, s, v)
    return

dist = [-1] * N
dist[0] = 0
dfs(0, 0)
#print(dist)
max_dist = max(dist)
max_v = dist.index(max_dist)

dist2 = [-1] * N
dist2[max_v] = 0
dfs2(max_v, max_v)
#print(dist2)

max_dist2 = max(dist2)
max_v2 = dist2.index(max_dist2)
dist3 = [-1] * N
dist3[max_v2] = 0
dfs3(max_v2, max_v2)
#print(dist3)

for v in range(N):
    if v == max_v:
        print(dist3[v] - D[v] + D[max_v2])
    elif v == max_v2:
        print(dist2[v] - D[v] + D[max_v])
    else:
        print(max(dist2[v] - D[v] + D[max_v], dist3[v] - D[v] + D[max_v2]))
    

