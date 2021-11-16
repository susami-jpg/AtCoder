# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 11:50:28 2021

@author: kazuk
"""

n = 5
edge = [[1,2,3],[0,2],[0,1],[0,4],[3]] # False
#edge = [[1,3],[0,2],[1,3],[0,2,4],[3]] # True


"""
n, m = map(int, input().split())
edge = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    edge[u-1].append(v-1)
    edge[v-1].append(u-1)
"""

#二部グラフ判定　再帰ver
from sys import setrecursionlimit
setrecursionlimit(10**7)

#dfs(v, c)は頂点vをc色に塗った時に矛盾がないかを判定する
#n個の頂点の色を初期化。0:未着色、1:黒、-1:白
color = [0] * n
def dfs(v, c):
    color[v] = c
    for nextv in edge[v]:
        #隣接頂点が同じ色なら矛盾
        if color[nextv] == c:
            return False
        #隣接頂点を違う色に塗った場合の評価がFalseなら矛盾
        if color[nextv] == 0 and not dfs(nextv, -c):
            return False
    #矛盾がなければTrue
    return True

def is_bipartite():
    return dfs(0, 1) #頂点0を黒(1)に塗ってdfs開始

print(is_bipartite())



"""
n, m = map(int, input().split())
edge = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    edge[u-1].append(v-1)
    edge[v-1].append(u-1)
"""
#二部グラフ判定　非再帰ver
#2部グラフならTrue, そうでなければFalse
#n個の頂点の色を初期化。0:未着色、1:黒、-1:白
color = [0] * n

def is_bipartite():
    stack = [(0, 1)] #(頂点、色)のタプルをスタックする。最初は(頂点0, 黒(1))
    while stack:
        v, c = stack.pop()
        #今いる点を着色
        color[v] = c
        #今の頂点から行けるところをチェック
        for nextv in edge[v]:
            #同じ色が隣接してしまったらFalse
            if color[nextv] == c:
                return False
            #未着色の頂点があったら反転した色と共にスタックに積む
            if color[nextv] == 0:
                stack.append((nextv, -c))
    #調べ終わったら矛盾がないのでTrue
    return True

print(is_bipartite())