from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt, factorial, floor
from copy import copy, deepcopy
INF = 10**20
MOD = 10**9+7

N, M = map(int, input().split())
edge = [[] for _ in range(N)]
for _ in range(M):
    a, b, c, d = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append((b, c, d))
    edge[b].append((a, c, d))
    
#目的関数
#(t+1) + (Di/(t+1))について、
#相加相乗平均より√D-1のとき、最小値2√Dをとる
def f(c, t, d):
    return t + c + floor(d/(t+1))

def dijkstra(s, g):
    dist = [INF] * N
    fix = [False] * N
    hq = [(0, s)]
    dist[s] = 0
    while hq:
        _, v = heappop(hq)
        fix[v] = True
        for nextv, c, d in edge[v]:
            fastest = INF
            time = INF
            for t in range(max(0, floor(sqrt(d))-3), floor(sqrt(d))+3):
                if fastest > f(c, t, c):
                    fastest = f(c, t, d)
                    time = t
            if time >= dist[v]:
                cost = f(c, time, d)
            else:
                cost = f(c, dist[v], d)
            if dist[nextv] > cost:
                dist[nextv] = cost
                heappush(hq, (dist[nextv], nextv))
    return dist[g]

ans = dijkstra(0, N-1)
if ans >= INF:
    print(-1)
else:
    print(ans)
    

 