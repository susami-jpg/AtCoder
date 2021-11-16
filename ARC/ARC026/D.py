from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

N, M = map(int, input().split())
edge = [tuple(map(int, input().split())) for _ in range(M)]

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
        return ''.join(f'{r}: {m}' for r, m in self.all_group_members().items())

def is_ok(x):
    weited_edge = []
    for a, b, c, t in edge:
        w = c - t*x
        weited_edge.append((w, a, b))
    weited_edge.sort()
    
    uf = UnionFind(N)
    cost = 0
    cnt = 0
    for w, a, b in weited_edge:
        if w <= 0:
            cost += w
            if uf.same(a, b):continue
            uf.union(a, b)
        else:
            if uf.same(a, b):continue
            cost += w
            uf.union(a, b)

    if cost <= 0:
        return True
    else:
        return False

ok = 10**15
ng = 0

for _ in range(100):
    mid = (ng+ok)/2
    if is_ok(mid):
        ok = mid
    else:
        ng = mid

print(ok)
