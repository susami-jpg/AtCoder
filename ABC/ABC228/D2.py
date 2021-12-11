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

setrecursionlimit(10**7)
N = 2**20
par = [-1] * (N+1)
def find(x):
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

def unite(x, y):
    x = find(x)
    y = find(y)
    if x == y:return
    if x < y:
        x, y = y, x
    par[x] += par[y]
    par[y] = x
    return

Q = int(input())
ans = [-1] * N
for _ in range(Q):
    t, x = map(int, input().split())
    if t == 1:
        h = x%N
        target = find(h)
        if target == N:
            target = find(0)
        ans[target] = x
        unite(target, target+1)
    else:
        x %= N
        print(ans[x])
        