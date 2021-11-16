# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 10:08:34 2021

@author: kazuk
"""

"""
Qiita オイラーツアーした木に対するクエリ参照 https://qiita.com/recuraki/items/72e37eb9be9f71bc623a

visit: STEPで訪れた頂点の番号(1-index)
vcost1: 初めて訪れた際のその頂点のコスト(本例では頂点コストは頂点番号に等しくしている)
vcost2: 初めて訪れた際のその頂点のコスト と 最後に訪れた際のコストをマイナスで記録したもの
ecost1: 初めて通った辺のコスト
ecost2: 初めて通った辺のコスト と 最後にその辺を訪れた時のコストをマイナスで記録したもの
depth: その頂点の深さ

深さ: 根を0とした時の頂点の深さ
Discovery: その頂点を最初に訪れた時間(STEP)
Finishing: その頂点を抜けた時間(STEP) つまり、その頂点を最後に訪れた時間+1
Finishing は「最後に訪れた時間」ではなく「抜けた時間」です
"""

time = 0
#max_stepは深さ優先探索での探索回数(nodeを訪れる回数)より大きく見積もる"
#深さ優先探索はO(V+E)なのでその10倍くらいとっておけばok?
max_step = 10**7
"""
n, m = map(int, input().split())
G = [[] for _ in range(n)]
for _ in range(m):
    u, v, c = map(int, input().split())
    u -= 1
    v -= 1
    G[u].append((v, c))
    G[v].append((u, c))
"""
n, m = 6, 5
G = [[(1, 2), (5, 6)], [(0, 2), (2, 3), (4, 5)], [(1, 3), (3, 4)], [(2, 4)], [(1, 5)], [(0, 6)]]

visit = [0] * max_step
vcost1 = [0] * max_step
vcost2 = [0] * max_step
ecost1 = [0] * max_step
ecost2 = [0] * max_step
depth = [0] * max_step

node_depth = [-1] * n
Discovery = [-1] * n
Finishing = [-1] * n

def dfs(v, G, d, c):
    global time
    if Discovery[v] == -1:
        Discovery[v] = time
        node_depth[v] = d
        vcost1[time] = v+1 #ここでは頂点コスト=頂点番号としている
        vcost2[time] = v+1
    depth[time] = d
    visit[time] = v+1
    time += 1
    for nextv, cost in G[v]:
        if Discovery[nextv] == -1:
            ecost1[time] = cost
            ecost2[time] = cost
            dfs(nextv, G, d+1, cost)
            depth[time] = d
            visit[time] = v+1
            time += 1
    Finishing[v] = time
    vcost2[time] = -(v+1)
    if c >= 0:
        ecost2[time] = -c
    return

dfs(0, G, 0, -1)

#stepは深さ優先探索終了までの探索回数(time)
visit = visit[:time+1]
vcost1 = vcost1[:time+1]
vcost2 = vcost2[:time+1]
ecost1 = ecost1[:time+1]
ecost2 = ecost2[:time+1]
print(visit)
print(vcost1)
print(vcost2)
print(ecost1)
print(ecost2)
print(Discovery)
print(Finishing)
print(node_depth)

#seg木パート/多次元配列用
class SegTree_dim:
    """
    init(init_val, ide_ele): 配列init_valで初期化 O(N)
    update(k, x): k番目の値をxに更新 O(logN)
    query(l, r): 区間[l, r)をsegfuncしたものを返す O(logN)
    """
    def __init__(self, init_val, segfunc, ide_ele):
        """
        init_val: 配列の初期値
        segfunc: 区間にしたい操作
        ide_ele: 単位元
        n: 要素数
        num: n以上の最小の2のべき乗
        tree: セグメント木(1-index)
        """
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        # 配列の値を葉にセット
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        # 構築していく
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])
            

    def update(self, k, x):
        """
        k番目の値をxに更新
        k: index(0-index)
        x: update value
        """
        k += self.num
        self.tree[k][0] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        """
        [l, r)のsegfuncしたものを得る
        l: index(0-index)
        r: index(0-index)
        """
        res = self.ide_ele

        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res

#LCA
#多次元配列の用意([depth, visit]となる多次元配列)
lca = []
for i in range(len(visit)):
    lca.append([depth[i], visit[i]])

#####segfunc#####
#min用のsegfunc
def segfunc(x, y):
    if x[0] > y[0]:
        return y
    else:
        return x
#################

#####ide_ele#####
ide_ele = [float('inf'), -1]
#################

lca = SegTree_dim(lca, segfunc, ide_ele)

#LCA(x, y)は頂点x, yの最近共通祖先の頂点を返す
def LCA(x, y):
    #LCAパート
    #RMQをとる範囲の
    discovery_xtime = Discovery[x-1]
    discovery_ytime = Discovery[y-1]
    finishing_xtime = Finishing[x-1]
    finishing_ytime = Finishing[y-1]
    
    discovery_time = min(discovery_xtime, discovery_ytime)
    finishing_time = max(finishing_xtime, finishing_ytime)
    
    return lca.query(discovery_time, finishing_time)[1]
    

#普通のseg木
class SegTree:
    """
    init(init_val, ide_ele): 配列init_valで初期化 O(N)
    update(k, x): k番目の値をxに更新 O(logN)
    query(l, r): 区間[l, r)をsegfuncしたものを返す O(logN)
    """
    def __init__(self, init_val, segfunc, ide_ele):
        """
        init_val: 配列の初期値
        segfunc: 区間にしたい操作
        ide_ele: 単位元
        n: 要素数
        num: n以上の最小の2のべき乗
        tree: セグメント木(1-index)
        """
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        # 配列の値を葉にセット
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        # 構築していく
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        """
        k番目の値をxに更新
        k: index(0-index)
        x: update value
        """
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        """
        [l, r)のsegfuncしたものを得る
        l: index(0-index)
        r: index(0-index)
        """
        res = self.ide_ele

        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res


#頂点xを根とする部分木の頂点のコストと辺のコストの合計

#####segfunc#####
#sumのsegfunc
def segfunc(x, y):
    return x+y
#################

#####ide_ele#####
ide_ele = 0
#################

part_node_seg = SegTree(vcost1, segfunc, ide_ele)
part_edge_seg = SegTree(ecost1, segfunc, ide_ele)

#xは1indexのnodeを渡す
def part_node_sum(x):
    l = Discovery[x-1]
    r = Finishing[x-1]
    return part_node_seg.query(l, r)

#xは1indexのnodeを渡す
def part_edge_sum(x):
    l = Discovery[x-1] + 1
    r = Finishing[x-1]
    return part_edge_seg.query(l, r)



#根からのパスクエリ(最短経路での辺と頂点の和)
#####segfunc#####
#sumのsegfunc
def segfunc(x, y):
    return x+y
#################

#####ide_ele#####
ide_ele = 0
#################

pass_node_seg = SegTree(vcost2, segfunc, ide_ele)
pass_edge_seg = SegTree(ecost2, segfunc, ide_ele)

#xは1indexのnodeを渡す
def pass_node_sum(x):
    r = Discovery[x-1]+1
    return pass_node_seg.query(0, r)

#xは1indexのnodeを渡す
def pass_edge_sum(x):
    r = Discovery[x-1]+1
    return pass_edge_seg.query(1, r)


#任意の２点間の距離
#x, yは1indexのnodeを渡す
def node_sum_x_to_y(x, y):
    lca = LCA(x, y)
    #ここではnodeの重みを頂点番号としている(任意で変更する)
    return pass_node_sum(x) + pass_node_sum(y) - 2 * pass_node_sum(lca) + lca

#x, yは1indexのnodeを渡す
def edge_sum_x_to_y(x, y):
    lca = LCA(x, y)
    return pass_edge_sum(x) + pass_edge_sum(y) - 2 * pass_edge_sum(lca)
