from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt, factorial
from decimal import Decimal
#decimalには文字列で渡す PyPyは遅いのでPython3で提出する
#d1 = Decimal('1.1') d2 = Decimal('2.3') -> d1 + d2などの演算で浮動小数点数での誤差がなくなる(割り算もok)
INF = 10**15
MOD = 10**9+7

N, M = map(int, input().split())
edge = [[] for _ in range(N)]
edge_id = dict()
for i in range(M):
    s, t = map(int, input().split())
    s -= 1
    t -= 1
    edge[s].append((t, i))
    edge_id[(s, t)] = i

dist = [INF] * N
dist[0] = 0
deq = deque()
deq.append(0)
prev = [-1] * N
while deq:
    v = deq.popleft()
    for nextv, i in edge[v]:
        if dist[nextv] > dist[v] + 1:
            dist[nextv] = dist[v] + 1
            deq.append(nextv)
            prev[nextv] = v

min_dist = dist[N-1]
#print(prev)
#print(dist)
cur = N-1
used_edge = set()
while prev[cur] != -1:
    used_edge.add(edge_id[(prev[cur], cur)])
    cur = prev[cur]

for ban in range(M):
    if ban in used_edge:
        dist = [INF] * N
        dist[0] = 0
        deq = deque()
        deq.append(0)
        while deq:
            v = deq.popleft()
            for nextv, i in edge[v]:
                if i == ban:continue
                if dist[nextv] > dist[v] + 1:
                    dist[nextv] = dist[v] + 1
                    deq.append(nextv)
        
        if dist[N-1] == INF:
            print(-1)
        else:
            print(dist[N-1])
            
    else:
        if min_dist == INF:
            print(-1)
        else:
            print(min_dist)
        