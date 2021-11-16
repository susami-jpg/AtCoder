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
N, M = map(int, input().split())
edges = []
cost = [0] * M
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
    par[x] += par[y]
    par[y] = x
    return

def same(x, y):
    return find(x) == find(y)

for i in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    cost[i] = c
    edges.append((c, a, b, i))

edges.sort()
unused = [1] * M
for c, a, b, i in edges:
    if c <= 0:
        unite(a, b)
        unused[i] = 0
    else:
        if same(a, b):continue
        unused[i] = 0
        unite(a, b)
ans = 0
for i in range(M):
    if unused[i]:
        ans += cost[i]
print(ans)

