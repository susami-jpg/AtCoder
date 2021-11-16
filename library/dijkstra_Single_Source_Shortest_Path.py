# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 15:52:14 2021

@author: kazuk
"""
from heapq import heappop, heappush
INF = 10 ** 10
v, e, r = map(int, input().split())
adj = [[] for _ in range(v)]
for _ in range(e):
    s, t, d = map(int, input().split())
    adj[s].append((t, d))

def dijkstra(s):
     #スタート地点を0に、他をinfにして初期化
    dis = [INF] * v
    dis[s] = 0
    fix = [False] * v
    hq = [[0, s]]
    while hq:
        now = heappop(hq)[1]
        #nowは現在未確定の頂点の候補の中で最小の頂点なので値を確定させる
        fix[now] = True
        #nowに隣接した頂点をひとつずつ見ていき、未確定かつ現在の距離の値より小さければ更新
        for nextv, w in adj[now]:
            if fix[nextv] == False:
                dis[nextv] = min(dis[nextv], dis[now] + w)
                #heapqは二次元配列の場合要素の先頭について小さい順に並ぶ
                heappush(hq, (dis[nextv], nextv))
    return dis

ans = dijkstra(r)
for i in ans:
    if i == INF:
        print('INF')
    else:
        print(i)
        
    
                
    