# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 16:36:31 2021

@author: kazuk
"""

#graphは第一要素に子ノード、第二要素に重みがくるようなタプルをリストで保存
#O(|E|log|V|) (E:辺の数, V:頂点数)
n, m = map(int, input().split())
G = [[] for _ in range(n)]
for _ in range(m):
    u, v, c = map(int, input().split())
    G[u].append((v, c))
    G[v].append((u, c))

def dijkstra(s, graph): # (始点, グラフのリスト)
    from heapq import heappop, heappush
    INF = 10 ** 18
    dist = [INF] * n # INF で初期化
    check = [False] * n # Bool
    dist[s] = 0
    q = [(0, s)] # （距離・ノード）
    while q:
        v = heappop(q)[1] # 今いるノード
        if check[v]: continue # すでに行っていたらcontinue
        check[v] = True # 訪問済み
        for nextv, cost in graph[v]: # 先のノード・距離
            if check[nextv] != False: continue
            if dist[nextv] <= dist[v] + cost: continue
            dist[nextv] = dist[v] + cost
            heappush(q, (dist[nextv], nextv)) # 必ず[0]が距離になるように（優先度付きキュー）
    return dist


#最短経路復元用
def dijkstra_rec(s, graph): # (始点, グラフのリスト)
    from heapq import heappop, heappush
    INF = 10 ** 18
    dist = [INF] * n # INF で初期化
    check = [False] * n # Bool
    dist[s] = 0
    q = [(0, s)] # （距離・ノード）
    prev = [-1] * n # ひとつ前にどのノードにいたか
    while q:
        v = heappop(q)[1] # 今いるノード
        if check[v]: continue # すでに行っていたらcontinue
        check[v] = True # 訪問済み
        for nextv, cost in graph[v]: # 先のノード・距離
            if check[nextv] != False: continue
            if dist[nextv] <= dist[v] + cost: continue
            dist[nextv] = dist[v] + cost
            prev[nextv] = v
            heappush(q, (dist[nextv], nextv)) # 必ず[0]が距離になるように（優先度付きキュー）
    return dist, prev

#最短経路復元
def get_path(g, prev):
    path = []
    now = g
    while now != -1:
        path.append(now)
        now = prev[now]
    path.reverse()
    return path

dist, prev = dijkstra_rec(0, G)
print(get_path(n-1, prev))

