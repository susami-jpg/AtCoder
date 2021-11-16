# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 09:33:45 2021

@author: kazuk
"""

from collections import deque

#nは頂点数、adjはコスト付きの隣接リスト
def bfs_num(n, adj):
    INF = 10**10
    mod = 10**9+7
    deq = deque()
    dist = [INF] * n
    num = [0] * n
    dist[0] = 0
    num[0] = 1
    deq.append(0)
    
    while deq:
        v, w = deq.popleft()
        if dist[v] < w:continue
        for nextv, cost in adj[v]:
            if dist[nextv] > dist[v] + cost:
                dist[nextv] = dist[v] + cost
                num[nextv] = num[v]
            elif dist[nextv] == dist[v] + cost:
                num[nextv] += num[v]
                num[nextv] %= mod
    return dist[-1], num[-1]



from heapq import heappop, heappush

def dijkstra_num(n, adj):
    INF = 10**10
    mod = 10**9+7
    dist = [INF] * n
    num = [0] * n
    hq = [(0, 0)]
    dist[0] = 0
    num[0] = 1
    
    while hq:
        w, v = heappop(hq)[1]
        if dist[v] < w:continue
        for nextv, cost in adj[v]:
            if dist[nextv] > dist[v] + cost:
                dist[nextv] = dist[v] + cost
                num[nextv] = num[v]
                heappush(hq, (dist[nextv], nextv))
            elif dist[nextv] == dist[v] + cost:
                num[nextv] += num[v]
                num[nextv] %= mod
    return dist[-1], num[-1]


                
    
    
    