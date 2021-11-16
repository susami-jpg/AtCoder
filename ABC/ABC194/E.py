from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7
"""
N, M = map(int, input().split())
A = list(map(int, input().split()))
rec = defaultdict(list)
for i in range(N):
    rec[A[i]].append(i)

mex = 0
while 1:
    if len(rec[mex]) == 0:
        print(mex)
        exit()
    prev = -1
    for nxt in rec[mex]:
        if nxt-prev-1 >= M:
            print(mex)
            exit()
        prev = nxt
    if N-1-prev >= M:
        print(mex)
        exit()
    mex += 1
"""

"""
N, M = map(int, input().split())
A = list(map(int, input().split()))

def is_ok(x):
    #x以下の数が何種類あるか?
    kinds = 0
    rec = [0] * N
    #defaultdictでやるとTLE
    #rec = defaultdict(int)
    for i, a in enumerate(A):
        if i-M >= 0:
            if A[i-M] <= x and rec[A[i-M]] == 1:
                kinds -= 1
            rec[A[i-M]] -= 1
        if a <= x and rec[a] == 0:
            kinds += 1
        rec[a] += 1
        if i >= M-1 and kinds <= x:
            return True
    else:
        return False


def meguru_bisect(ng, ok):
    '''
    初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
    まずis_okを定義すべし
    ng ok は  とり得る最小の値-1 とり得る最大の値+1
    最大最小が逆の場合はよしなにひっくり返す
    '''
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

ans = meguru_bisect(-1, N)
print(ans)
"""

'''
その他の操作（最小値以外）
操作	segfunc	単位元
最小値	min(x, y)	float('inf')
最大値	max(x, y)	-float('inf')
区間和	x + y	0
区間積	x * y	1
最大公約数	math.gcd(x, y)	0
'''

#####segfunc#####
def segfunc(x, y):
    return min(x, y)

#################

#####ide_ele#####
ide_ele = INF
#################

class SegTree:
    '''
    init(init_val, ide_ele): 配列init_valで初期化 O(N)
    update(k, x): k番目の値をxに更新 O(logN)
    query(l, r): 区間[l, r)をsegfuncしたものを返す O(logN)
    '''

    def __init__(self, init_val, segfunc, ide_ele):
        '''
        init_val: 配列の初期値
        segfunc: 区間にしたい操作
        ide_ele: 単位元
        n: 要素数
        num: n以上の最小の2のべき乗
        tree: セグメント木(1-index)
        '''
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
        '''
        k番目の値をxに更新
        k: index(0-index)
        x: update value
        '''
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        '''
        [l, r)のsegfuncしたものを得る
        l: index(0-index)
        r: index(0-index)
        '''
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
    
N, M = map(int, input().split())
A = list(map(int, input().split()))

seg = SegTree([i for i in range(N+1)], segfunc, ide_ele)
cnt = [0] * N
ans = INF
for i in range(N):
    if i-M >= 0:
        if cnt[A[i-M]] == 1:
            seg.update(A[i-M], A[i-M])
        cnt[A[i-M]] -= 1
    if cnt[A[i]] == 0:
        seg.update(A[i], INF)
    cnt[A[i]] += 1
    if i >= M-1:
        ans = min(ans, seg.query(0, N+1))

print(ans)

        
        

                    