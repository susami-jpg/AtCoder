# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 01:46:44 2021

@author: kazuk
"""

"""
クラスカル法：
O(|E|log|V|)

辺集合 E をコストの小さい順にソートする
以下を V−1 個の辺を選ぶまで（最小全域木 T ができるまで）繰り返す
残っている辺の中からコストが最小の辺 e を取り出す。現在構成中の T に e を加えても閉路ができないなら T に加える。
"""

#UnionFind
from collections import defaultdict

#UnionFindのNodeは0indexであることに注意
class UnionFind():
    def __init__(self, n):
        self.n = n
#parents
#各要素の親要素の番号を格納するリスト
#要素が根（ルート）の場合は-(そのグループの要素数)を格納する
        self.parents = [-1] * n
#find(x)
#要素xが属するグループの根を返す
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

#union(x, y)
#要素xが属するグループと要素yが属するグループとを併合する
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

#size(x)
#要素xが属するグループのサイズ（要素数）を返す
    def size(self, x):
        return -self.parents[self.find(x)]

#same(x, y)
#要素x, yが同じグループに属するかどうかを返す
    def same(self, x, y):
        return self.find(x) == self.find(y)

#members(x)
#要素xが属するグループに属する要素をリストで返す
    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

#roots()
#すべての根の要素をリストで返す
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

#group_count()
#グループの数を返す
    def group_count(self):
        return len(self.roots())
    
#all_group_members
#{ルート要素: [そのグループに含まれる要素のリスト], ...}のdefaultdictを返す
#defaultdictは辞書dictのサブクラス
#print(uf.all_group_members())
# {0: [0, 2], 1: [1, 3, 4, 5]}
#print(list(uf.all_group_members().values()))
# [[0, 2], [1, 3, 4, 5]]
    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members
    
#all_group_size
#すべてのグループのサイズを返す
    def all_group_size(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        group_members = list(map(len, list(group_members.values())))
        return group_members

#__str__()
#print()での表示用
#ルート要素: [そのグループに含まれる要素のリスト]を文字列で返す
    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())
    
"""
n, m = map(int, input().split())
edge = []
for _ in range(m):
    f, t, w = map(int, input().split())
    edge.append((w, f-1, w-1))
"""

#edgeは(辺の重み, from, to)をの順で辺の情報を持ったリスト
def Kruskal(n, edge):
    uf = UnionFind(n)
    edge.sort()
    ans = 0
    cnt = 0
    for w, f, t in edge:
        if cnt == n-1:break
        if uf.same(f, t):continue
        ans += w
        cnt += 1
        uf.union(f, t)
    return ans
    
    


"""
プリム法：
O(|E|log|V|)

はじめに、適当に選んだ頂点 1 つのみを T に含めると確定させる
以下をすべての頂点が T に含まれるまで繰り返す
全ての「既に確定した頂点」から「まだ確定していない（T に含まれていない）頂点 」へ伸びる辺を全て確認して、最小のコストの辺 e=(u,v) を選ぶ。そして v を T に含めることにする。

"""
"""
n, m = map(int, input().split())
edge = [[] for _ in range(n)]
for _ in range(m):
    f, t, w = map(int, input().split())
    edge[f-1].append((t-1, w))
    edge[t-1].append((f-1, w))
"""

from heapq import heappush, heappop, heapfy
#Gは隣接リスト(グラフ)
def Prim(n, edge):
    used = [0] * n
    #適当に選んだ頂点0をTに含める
    used[0] = 1
    hq = [(w, v) for v, w in edge[0]]
    heapfy(hq)
    ans = 0
    while hq:
        w, v = heappop(hq)
        if used[v]:continue
        used[v] = 1
        ans += w
        for nextv, w in edge[v]:
            if used[nextv]:continue
            heappush(hq, (w, nextv))
    return ans


        