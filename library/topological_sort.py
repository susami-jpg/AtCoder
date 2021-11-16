# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 16:48:10 2021

@author: kazuk
"""

"""
計算量 O(V+E)

Wikipediaではトポロジカルソートのアルゴリズムは以下のようになっています。

L ← トポロジカルソートした結果を蓄積する空リスト
S ← 入力辺を持たないすべてのノードの集合

while S が空ではない do
    S からノード n を削除する
    L に n を追加する
    for each n の出力辺 e とその先のノード m do
        辺 e をグラフから削除する
        if m がその他の入力辺を持っていなければ then
            m を S に追加する

if グラフに辺が残っている then
    閉路があり DAG でないので中断
"""

#トポロジカルソート
from collections import deque

def topological_sort():
    def chmax(a, b):
        if a >= b:
            return a
        else:
            return b
        
    n, m = map(int, input().split())
    edge = [[] for _ in range(n)]
    
    #各頂点の入力辺の本数を記録
    deg = [0] * n
    for _ in range(m):
        x, y = map(int, input().split())
        edge[x - 1].append(y - 1)
        deg[y - 1] += 1
    
    #入力辺を持たない頂点をqueueにいれる
    que = deque()
    for v in range(n):
        if deg[v] == 0:
            que.append(v)
    
    #各頂点の最初に入力辺を持たなかった点からの距離
    dp = [0] * n
    topo = []
    #queに同時に複数のノードが入っている瞬間があると、pop時にどれが選ばれるかによってソート結果が変わる。
    #よってqueに複数のノードが入っている瞬間がある=複数のトポロジカルソートがあると判定できる
    #ここで、例えばqueに優先度キューを用いるとノードIDが小さい順に取り出され、小さいノードを優先して前に持ってくるよう固定される。
    while que:
        v = que.popleft()
        topo.append(v)
        for nextv in edge[v]:
            #辺(v, nextv)をグラフから削除する
            deg[nextv] -= 1
            if deg[nextv] == 0:
                que.append(nextv)
            #最初に入力辺を持たなかった点からの距離
            dp[nextv] = chmax(dp[nextv], dp[v] + 1)
    
    #閉路の場合-1を返す
    if len(topo) != n:
        return -1
    else:
        return topo
    
"""
深さ優先探索(DFS)でのアルゴリズム：

まだ未探索の頂点があれば以下を繰り返す
深さ優先探索を行い、帰りがけの順に頂点を採用する
採用した頂点はトポロジカルソートの順序と逆向きなので、反転させる
"""


import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

#メモ化再帰
def memo():
    def chmax(a, b):
        if a >= b:
            return a
        else:
            return b
        
    #頂点数n、辺数m
    n, m = map(int, input().split())
    edge = [[] for _ in range(n)]
    #0-indexedに変更
    for _ in range(m):
        x, y = map(int, input().split())
        edge[x - 1].append(y - 1)
        
    # dp[v] := ノードvを始点とした時の有向パスの長さの最大値
    # -1 未訪問で初期化。
    dp = [-1] * n
    
    #関数recはノードvを始点としたときの有向パスの長さの最大値を返す関数
    def rec(v):
        if dp[v] != -1:
            return dp[v]
        ans = 0
        for nextv in edge[v]:
            ans = chmax(ans, rec(nextv) + 1)
        dp[v] = ans
        return dp[v]
    
    #有効グラフ全体としての最長パスを見つける
    ans = 0
    for v in range(n):
        ans = chmax(ans, rec(v))   
    print(ans)


from collections import deque
def topological_sort_bfs(graph):
    # トポロジカルソートした結果を蓄積する空リスト
    topological_sorted_list = []
    queue = deque()
    # 入力辺を持たないすべてのノードの集合
    for vertex in graph:
        indegree = vertex.get_indegree()
        if indegree == 0:
            queue.append(vertex)
    # while S が空ではない do
    while len(queue) > 0:
        # S からノード n を削除する
        current_vertex = queue.popleft()
        # L に n を追加する
        topological_sorted_list.append(current_vertex.get_vertex_id())
        # for each n の出力辺 e とその先のノード m do
        for neighbor in current_vertex.get_connections():
            # 辺 e をグラフから削除する
            neighbor.set_indegree(neighbor.get_indegree() - 1)
            # if m がその他の入力辺を持っていなければ then
            if neighbor.get_indegree() == 0:
                # m を S に追加する
                queue.append(neighbor)
    if len(topological_sorted_list) != len(graph.get_vertices()):
        #print("Kahn's algorithm:", '閉路があります。DAGではありません。')
        return -1
    else:
        #print("Kahn's algorithm tological sorted list:", topological_sorted_list)
        return topological_sorted_list




def topological_sort_dfs(graph):
    # L ← トポロジカルソートされた結果の入る空の連結リスト
    topological_reverse_sorted_list = []
    try:
        # for each ノード n do
        for current_vertex in graph:
            # if n に permanent の印が付いていない then
            if not(current_vertex.permanent):
                topological_sort_dfs_visit(current_vertex, topological_reverse_sorted_list)
    # 閉路を発見した場合
    except GraphTopologicalError:
        print('DFS algorithm:', '閉路があります。DAGではありません。')
    else:
        # リストは最後から読み出す
        print("DFS algorithm tological sorted list:", topological_reverse_sorted_list[::-1])
        
def topological_sort_dfs_visit(vertex, topological_sorted_list):
    if vertex.permanent:
        return
    # if n に「一時的」の印が付いている then
    if vertex.temporary:
        # 閉路があり DAG でないので中断
        raise GraphTopologicalError(topological_sorted_list)
    # n に「一時的」の印を付ける
    vertex.temporary = True
    # for each n の出力辺 e とその先のノード m do
    for neighbor in vertex.get_connections():
        topological_sort_dfs_visit(neighbor, topological_sorted_list)
    vertex.temprary = False
    # n に「恒久的」の印を付ける
    vertex.permanent = True
    # n を L に追加
    topological_sorted_list.append(vertex.get_vertex_id())


