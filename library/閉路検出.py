# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 18:34:05 2021

@author: kazuk
"""

#閉路検出 dfs
from sys import setrecursionlimit
setrecursionlimit(10**7)
n, m = map(int, input().split())
adj = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    adj[u-1].append(v-1)
    adj[v-1].append(u-1)

seen = [0] * n
def dfs(v, par=-1):
    if seen[v]:
        return False
    seen[v] = 1
    ans = True
    for nextv in adj[v]:
        if nextv == par:
            continue
        ans &= dfs(nextv, v)
    return ans

ans = 0
for v in range(n):
    if dfs(v):
        ans += 1
print(ans)


#UnionFind(今見ている辺までに作成されたグループで、すでにその端点のグループが同じなら閉路)
"""
入力される辺を(Ai, Bi)とします．
Union-Find木を利用してAi, Biの親(グループ番号)を調べます．これをGA, GBとします．
GA=GBの時，この辺(Ai, Bi)を張った時点で閉路が発生します．
"""
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