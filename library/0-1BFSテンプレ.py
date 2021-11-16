# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 01:29:36 2021

@author: kazuk
"""
"""
頂点数を V 、辺数を E とします。よく使われる実装ではこのようになります。

ダイクストラ法（優先度付きキュー利用）：O(V+ElogV)
幅優先探索（キュー使用）：O(V+E)
01-BFS（両端キュー使用）：O(V+E)

01-BFSではまず始点を両端キューに加え、以下を繰り返します。

両端キューの先頭から頂点 v を取り出す。
頂点 v から伸びる辺を用いて暫定最短距離を更新できる頂点がある場合、更新してその頂点を
0の辺を用いた場合は両端キューの先頭に加える。
1の辺を用いた場合は両端キューの末尾に加える。
"""
from collections import deque

# 頂点数N、始点の頂点番号s
N, s = map(int, input().split())
# 隣接リスト。
# edges[i]の要素に(j, c)が含まれる時、iからjにコストcの辺が存在
edges = [[] for i in range(N)]

dist = [10**9]*N
dist[s] = 0
que = deque()
que.append(s)

while len(que) > 0:
    i = que.popleft()
    for j, c in edges[i]:
        d = dist[i] + c
        if d < dist[j]:
            dist[j] = d
            if c == 1:
                que.append(j)
            else:
                que.appendleft(j)