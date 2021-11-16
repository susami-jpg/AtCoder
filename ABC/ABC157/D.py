from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right
from math import sqrt
INF = 10**15
MOD = 10**9+7


from collections import defaultdict

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

N, M, K = map(int, input().split())
friend = [0] * N
block = [0] * N
uf = UnionFind(N)
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    uf.union(a, b)
    friend[a] += 1
    friend[b] += 1

for _ in range(K):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if uf.same(c, d):
        block[c] += 1
        block[d] += 1

ans = []
for i in range(N):
    #-1は自分自身
    friend_cnd = max(0, uf.size(i) - friend[i] - block[i] - 1)
    ans.append(friend_cnd)
print(*ans)




    

