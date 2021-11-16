from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 998244353

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
    return (x+y)%MOD

#################

#####ide_ele#####
ide_ele = 0
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

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [0] * 3001
for j in range(A[0], B[0]+1):
    dp[j] = 1

def acc(A):
    n = len(A)
    for i in range(1, n):
        A[i] += A[i-1]
    return A

dp_prev = acc(dp)
#dp_prev = SegTree(dp, segfunc, 0)
for i in range(1, N):
    #dp = SegTree([0] * 3001, segfunc, 0)
    dp = [0] * 3001
    for j in range(A[i], B[i] + 1):
        #cnd = dp_prev.query(0, j+1)
        cnd = dp_prev[j]
        #dp.update(j, cnd%MOD)
        dp[j] = cnd%MOD
    dp_prev = acc(dp)

#ans = dp.query(0, 3001)
ans = dp_prev[-1]
print(ans%MOD)
