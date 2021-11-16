# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 11:27:19 2021

@author: kazuk
"""
from collections import defaultdict

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

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



#Union-Find木（サイズバージョン）の実装
class UnionFindVerSize():
    def __init__(self, N):
        """ N個のノードのUnion-Find木を作成する """
        # 親の番号を格納する。自分が親だった場合は、自分の番号になり、それがそのグループの番号になる
        self._parent = [n for n in range(0, N)]
        # グループのサイズ（個数）
        self._size = [1] * N

    def find_root(self, x):
        """ xの木の根(xがどのグループか)を求める """
        if self._parent[x] == x: return x
        self._parent[x] = self.find_root(self._parent[x]) # 縮約
        return self._parent[x]

    def unite(self, x, y):
        """ xとyの属するグループを併合する """
        gx = self.find_root(x)
        gy = self.find_root(y)
        if gx == gy: return

        # 小さい方を大きい方に併合させる（木の偏りが減るので）
        if self._size[gx] < self._size[gy]:
            self._parent[gx] = gy
            self._size[gy] += self._size[gx]
        else:
            self._parent[gy] = gx
            self._size[gx] += self._size[gy]

    def get_size(self, x):
        """ xが属するグループのサイズ（個数）を返す """
        return self._size[self.find_root(x)]

    def is_same_group(self, x, y):
        """ xとyが同じ集合に属するか否か """
        return self.find_root(x) == self.find_root(y)

    def calc_group_num(self):
        """ グループ数を計算して返す """
        N = len(self._parent)
        ans = 0
        for i in range(N):
            if self.find_root(i) == i:
                ans += 1
        return ans


#Union-Find木（深さバージョン）の実装
class UnionFindVerDepth():
    def __init__(self, N):
        """ N個のノードのUnion-Find木を作成する """
        # 親の番号を格納する。自分が親だった場合は、自分の番号になり、それがそのグループの番号になる
        self._parent = [n for n in range(0, N)]
        # グループの深さ
        self._depth = [1] * N

    def find_root(self, x):
        """ xの木の根(xがどのグループか)を求める """
        if self._parent[x] == x: return x
        self._parent[x] = self.find_root(self._parent[x]) # 縮約
        return self._parent[x]

    def unite(self, x, y):
        """ xとyの属するグループを併合する """
        gx = self.find_root(x)
        gy = self.find_root(y)
        if gx == gy: return

        # 小さい方を大きい方に併合させる（木の偏りが減るので）
        if self._depth[gx] < self._depth[gy]:
            self._parent[gx] = gy
        else:
            self._parent[gy] = gx
            if self._depth[gx] == self._depth[gy]: self._depth[gx] += 1

    def get_depth(self, x):
        """ xが属するグループの深さを返す """
        return self._depth[self.find_root(x)]

    def is_same_group(self, x, y):
        """ xとyが同じ集合に属するか否か """
        return self.find_root(x) == self.find_root(y)

    def calc_group_num(self):
        """ グループ数を計算して返す """
        N = len(self._parent)
        ans = 0
        for i in range(N):
            if self.find_root(i) == i:
                ans += 1
        return ans




