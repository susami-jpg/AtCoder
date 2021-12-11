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
N = int(input())
edge = [[] for _ in range(N)]
for _ in range(N-1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    edge[u].append(v)
    edge[v].append(u)

ans = [0] * N

dist = [0] * N
#dp[v]:= vの子方向の子供の数
dp = [0] * N
def dfs(v, d, par=-1):
    dist[v] = d
    s = 1
    for nextv in edge[v]:
        if nextv == par:continue
        s += dfs(nextv, d+1, v)
    dp[v] = s
    return s
dfs(0, 0)
ans[0] = sum(dist)
def dfs2(v, par=-1):
    for nextv in edge[v]:
        if nextv == par:continue
        ans[nextv] = ans[v] - dp[nextv] + (N-dp[nextv])
        dfs2(nextv, v)
    return

dfs2(0)
for v in range(N):
    print(ans[v])
    

