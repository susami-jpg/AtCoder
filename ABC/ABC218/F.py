from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

N, M = map(int, input().split())
edge = [[] for _ in range(N)]
for i in range(M):
    s, t = map(int, input().split())
    s -= 1
    t -= 1
    edge[s].append((t, i))

back = [(-1, -1)] * N
def bfs(s, ban = -1):
    dist = [INF] * N
    deq = deque()
    deq.append((0, 0, -1, -1))
    while deq:
        v, d, prev, ind = deq.popleft()
        if dist[v] != INF:continue
        dist[v] = d
        back[v] = (prev, ind)
        for nextv, ind in edge[v]:
            if ind == ban:continue
            if dist[nextv] != INF:continue
            deq.append((nextv, d+1, v, ind))
    return dist

dist = bfs(0)
if dist[N-1] == INF:
    for _ in range(M):
        print(-1)
    exit()
    
original_route = []
used_edge = set()
now = N-1
while now != -1:
    original_route.append(now)
    now, ind = back[now]
    used_edge.add(ind)

original_len = dist[N-1]

for i in range(M):
    if i in used_edge:
        dist = bfs(0, i)
        if dist[N-1] == INF:
            print(-1)
        else:
            print(dist[N-1])
    else:
        print(original_len)

            
