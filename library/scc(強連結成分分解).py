# -*- coding: utf-8 -*-
"""
Created on Fri May 14 03:13:59 2021

@author: kazuk
"""

# 強連結成分分解(SCC): グラフGに対するSCCを行う
# 入力: <N>: 頂点サイズ, <G>: 順方向の有向グラフ, <RG>: 逆方向の有向グラフ
# 出力: (<ラベル数>, <各頂点のラベル番号>)
from sys import setrecursionlimit, stdin
setrecursionlimit(10**7)
input = stdin.readline

def scc(N, G, RG):
    order = []
    used = [0]*N
    group = [None]*N
    def dfs(s):
        used[s] = 1
        for t in G[s]:
            if not used[t]:
                dfs(t)
        order.append(s)
    def rdfs(s, col):
        group[s] = col
        used[s] = 1
        for t in RG[s]:
            if not used[t]:
                rdfs(t, col)
    for i in range(N):
        if not used[i]:
            dfs(i)
    used = [0]*N
    label = 0
    for s in reversed(order):
        if not used[s]:
            rdfs(s, label)
            label += 1
    return label, group

# 縮約後のグラフを構築
def construct(N, G, label, group):
    G0 = [set() for i in range(label)]
    GP = [[] for i in range(label)]
    for v in range(N):
        lbs = group[v]
        for w in G[v]:
            lbt = group[w]
            if lbs == lbt:
                continue
            G0[lbs].add(lbt)
        GP[lbs].append(v)
    return G0, GP

n, m = map(int, input().split())
G = [[] for _ in range(n)]
Gr = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    Gr[b].append(a)

#labelはグループの数
#groupは各頂点をindexで示した時にどのグループに属するかを示すリスト
#GPは各グループの要素を格納したリストの列挙
G = [[1, 3], [0, 2, 2], [], [2, 0]]
Gr = [[1, 3], [0], [1, 3, 1], [0]]

label, group = scc(4, G, Gr)
G0, GP = construct(4, G, label, group)


def count_scc_elems(GP):
    cnt = 0
    for e in GP:
        n = len(e)
        if n == 0:continue
        cnt += n*(n-1)//2
    return cnt