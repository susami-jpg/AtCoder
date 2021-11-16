from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right
from collections import defaultdict, deque
from heapq import heappop, heappush, heapify
from math import sqrt
INF = 10**15
MOD = 10**9+7

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

N = int(input())
Q = int(input())
uf = UnionFind(N)
ans = [""] * Q
Query = []
#nxt_sum[i] = A[i] + A[i+1]
nxt_sum = [0] * N
for i in range(Q):
    T, X, Y, V = map(int, input().split())
    if T == 0:
        uf.union(X-1, Y-1)
        nxt_sum[X-1] = V
    else:
        if uf.same(X-1, Y-1):
            Query.append((i, X-1, Y-1, V))

        else:
            ans[i] = "Ambiguous"

rec = defaultdict(list)

root_list = []
for _, group in dict(uf.all_group_members()).items():
    root = min(group)
    root_list.append(root)
    L = len(group)
    Y0 = [0] * L
    Y1 = [1] * L
    now = root
    while now < root+L-1:
        Y0[now+1-root] = nxt_sum[now] - Y0[now-root]
        Y1[now+1-root] = nxt_sum[now] - Y1[now-root]
        now += 1
    rec[root] = [Y0, Y1]

root_list.sort()
root_list.append(10**15)
for i, x, y, v in Query:
    ind = bisect_left(root_list, x)
    if root_list[ind] == x:
        root = x
    else:
        root = root_list[ind-1]
    x -= root
    y -= root
    Y0, Y1 = rec[root]
    x_diff = Y1[x] - Y0[x]
    y_diff = Y1[y] - Y0[y]
    val0 = (v - Y0[x]) * x_diff
    Y = val0 * y_diff + Y0[y]
    ans[i] = Y

for a in ans:
    if a != "":
        print(a)




    



