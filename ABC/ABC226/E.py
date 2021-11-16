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
MOD = 998244353

setrecursionlimit(10**7)
N, M = map(int, input().split())
par = [-1] * N
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
    par[y] += par[x]
    par[x] = y
    return

def size(x):
    x = find(x)
    return -par[x]

edge_cnt = [0] * N
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    unite(u, v)
    edge_cnt[u] += 1
    edge_cnt[v] += 1

#print(edge_cnt)
edge_size = [0] * N
for v in range(N):
    p = find(v)
    edge_size[p] += edge_cnt[v]

ans = 1
for v in range(N):
    if v != find(v):continue
    #print(size(v), edge_size[v])
    if size(v) != edge_size[v]//2:
        ans = 0
    else:
        ans *= 2
        ans %= MOD
print(ans)
