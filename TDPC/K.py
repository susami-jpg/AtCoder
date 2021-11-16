from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt, factorial
from decimal import Decimal
#decimalには文字列で渡す PyPyは遅いのでPython3で提出する
#d1 = Decimal('1.1') d2 = Decimal('2.3') -> d1 + d2などの演算で浮動小数点数での誤差がなくなる(割り算もok)
INF = 10**15
MOD = 10**9+7

class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
        self.depth = n.bit_length()
 
    def get(self, i):
        s = 0
        while i > 0:
            s = max(s, self.tree[i])
            i -= i & -i
        return s
 
    def add(self, i, x):
        while i <= self.size:
            self.tree[i] = max(self.tree[i], x)
            i += i & -i
 
    def lower_bound(self, x):
        """ 累積和がx以上になる最小のindexと、その直前までの累積和 """
        sum_ = 0
        pos = 0
        for i in range(self.depth, -1, -1):
            k = pos + (1 << i)
            if k <= self.size and sum_ + self.tree[k] < x:
                sum_ = max(sum_, self.tree[k])
                pos += 1 << i
        return pos + 1, sum_
    
def CC(A: list) -> list:
    '座標圧縮'
    #index -> 実際の値のdict
    B = {}
    #実際の値 -> indexのdict
    C = {}
    for i, j in enumerate(sorted(A)):
        B[i] = j
        C[j] = i
    return B, C

N = int(input())
C = []
right_set = set()
for _ in range(N):
    x, r = map(int, input().split())
    C.append((x-r, x+r))
    right_set.add(x+r)
C.append((-INF, -INF))
right_set.add(-INF)
right_set = list(right_set)
ind_to_x, x_to_ind = CC(right_set)
C.sort(reverse=True)
r_size = len(right_set)
bit = Bit(r_size)
prev = None
stack = []
for l, r in C:
    #print(l, r)
    if prev != l and stack:
        for ind, val in stack:
            bit.add(ind, val)
        stack = []
    ind_r = x_to_ind[r]
    #r未満のdpの最大値を取得
    cnd = bit.get(ind_r)
    #print(cnd)
    stack.append((ind_r+1, cnd+1))

ans = bit.get(r_size)
print(ans)

