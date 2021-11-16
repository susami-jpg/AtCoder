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
N, M = map(int, input().split())
edge = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append(b)
    edge[b].append(a)

seen = [0] * N
def dfs(v):
    if seen[v]:
        return
    seen[v] = 1
    vs.append(v)
    for nextv in edge[v]:
        dfs(nextv)
    return

def dfs2(i):
    global now
    if i == len(vs):
        now += 1
        #print(color)
        return
    v = vs[i]
    for c in range(3):
        for child in edge[v]:
            if color[child] == c:
                break
        else:
            color[v] = c
            dfs2(i+1)
            color[v] = -1
    return

ans = 1
for v in range(N):
    if seen[v]:continue
    vs = []
    dfs(v)
    #print(vs)
    now = 0
    color = [-1] * N
    color[vs[0]] = 0
    dfs2(1)
    #print(3*now)
    ans *= 3*now
print(ans)
