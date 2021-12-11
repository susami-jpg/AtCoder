from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt, factorial
from decimal import Decimal
#decimalには文字列で渡す PyPyは遅いのでPython3で提出する
#d1 = Decimal('1.1') d2 = Decimal('2.3') -> d1 + d2などの演算で浮動小数点数での誤差がなくなる(割り算もok)
INF = 10**18
MOD = 10**9+7
setrecursionlimit(10**7)

N = int(input())
edge = [[] for _ in range(N)]
for _ in range(N-1):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append((b, c))
    edge[b].append((a, c))

D = list(map(int, input().split()))
#dfs(v):= vから出発した時に最大の旅費となる町を返す
def dfs1(v, s, cost, par=-1):
    if s == v:
        res = (-INF, -1)
    else:
        res = (cost + D[v], v)
    for nextv, c in edge[v]:
        if nextv == par:continue
        res = max(res, dfs1(nextv, s, cost+c, v))
    return res

def dfs2(v, par=-1):
    for nextv , c in edge[v]:
        if nextv == par:continue
        dist1[nextv] = dist1[v] + c
        dfs2(nextv, v)
    return

def dfs3(v, par=-1):
    for nextv , c in edge[v]:
        if nextv == par:continue
        dist2[nextv] = dist2[v] + c
        dfs3(nextv, v)
    return


_, u = dfs1(0, 0, 0)
_, s = dfs1(u, u, 0)
dist1 = [0] * N
dfs2(u)
dist2 = [0] * N
dfs3(s)
for v in range(N):
    if v == u:
        print(dist1[s] + D[s])
    elif v == s:
        print(dist2[u] + D[u])
    else:
        print(max(dist1[v] + D[u], dist2[v] + D[s]))

