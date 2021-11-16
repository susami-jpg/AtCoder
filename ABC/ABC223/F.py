from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt, factorial
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7


#②遅延セグ木(区間加算用）
def segfunc(x,y):
    return min(x, y)

class LazySegTree_RAQ:
    def __init__(self,init_val,segfunc,ide_ele):
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1<<(n-1).bit_length()
        self.tree = [ide_ele]*2*self.num
        self.lazy = [0]*2*self.num
        for i in range(n):
            self.tree[self.num+i] = init_val[i]
        for i in range(self.num-1,0,-1):
            self.tree[i] = self.segfunc(self.tree[2*i], self.tree[2*i+1])
    def gindex(self,l,r):
        l += self.num
        r += self.num
        lm = l>>(l&-l).bit_length()
        rm = r>>(r&-r).bit_length()
        while r>l:
            if l<=lm:
                yield l
            if r<=rm:
                yield r
            r >>= 1
            l >>= 1
        while l:
            yield l
            l >>= 1
    def propagates(self,*ids):
        for i in reversed(ids):
            v = self.lazy[i]
            if v==0:
                continue
            self.lazy[i] = 0
            self.lazy[2*i] += v
            self.lazy[2*i+1] += v
            self.tree[2*i] += v
            self.tree[2*i+1] += v
    def add(self,l,r,x):
        ids = self.gindex(l,r)
        l += self.num
        r += self.num
        while l<r:
            if l&1:
                self.lazy[l] += x
                self.tree[l] += x
                l += 1
            if r&1:
                self.lazy[r-1] += x
                self.tree[r-1] += x
            r >>= 1
            l >>= 1
        for i in ids:
            self.tree[i] = self.segfunc(self.tree[2*i], self.tree[2*i+1]) + self.lazy[i]
    def query(self,l,r):
        self.propagates(*self.gindex(l,r))
        res = self.ide_ele
        l += self.num
        r += self.num
        while l<r:
            if l&1:
                res = self.segfunc(res,self.tree[l])
                l += 1
            if r&1:
                res = self.segfunc(res,self.tree[r-1])
            l >>= 1
            r >>= 1
        return res

N, Q = map(int, input().split())
S = [1 if c == "(" else -1 for c in list(input())]
T = list(accumulate(S))

seg = LazySegTree_RAQ(T, segfunc, float('inf'))
for _ in range(Q):
    q, l, r = map(int, input().split())
    l -= 1
    r -= 1
    if q == 1:
        left = S[l]
        right = S[r]
        if left == right:continue
        if left == 1:
            seg.add(r, N, 2)
            seg.add(l, N, -2)
        else:
            seg.add(l, N, 2)
            seg.add(r, N, -2)
        S[l], S[r] = S[r], S[l]
    else:
        start = 0
        if l-1 >= 0:
            start = seg.query(l-1, l)
        end = seg.query(r, r+1)
        rmq = seg.query(l, r+1)
        if end - start != 0 or rmq - start < 0:
            print("No")
        else:
            print("Yes")
            
        

