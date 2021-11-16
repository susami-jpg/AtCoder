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
def f(k, t, d):
    return k + d/(t+k+1)

def ternary_search2(k, d):
    bottom = 0
    top = INF
    while abs(top-bottom) > 1:
        mid = (top + bottom) / 2
        if f(mid-1, k, d) > f(mid, k, d):
            bottom = mid
        else:
            top = mid
    return f(bottom, k, d)

def ternary_search(t, d, low=0, high=INF):
    while abs(high-low) > 1:
        c1 = (low*2 + high) / 3
        c2 = (low + high*2) / 3
        
        #もしf(c2)のほうがいい(小さい)なら、ダメなほうlowを更新する
        if f(c1, t, d) > f(c2, t, d):
            low = c1
        else:
            high = c2
    
    return f(low, t, d)

def dijkstra(s, g):
    dist = [INF] * N
    fix = [False] * N
    hq = [(0, s)]
    dist[s] = 0
    while hq:
        _, v = heappop(hq)
        fix[v] = True
        for nextv, c, d in edge[v]:
            cost = c + floor(ternary_search2(dist[v], d))
            if dist[nextv] > dist[v] + cost:
                dist[nextv] = dist[v] + cost
                heappush(hq, (dist[nextv], nextv))
    return dist[g]

ans = dijkstra(0, N-1)
if ans >= INF:
    print(-1)
else:
    print(ans)
    

 