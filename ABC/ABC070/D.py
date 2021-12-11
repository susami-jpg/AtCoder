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

def dfs(v, par=-1):
    for nextv, c in edge[v]:
        if par == nextv:continue
        if dp[nextv] != INF:continue
        dp[nextv] = dp[v] + c
        dfs(nextv, v)
    return

dp = [INF] * N
Q, K = map(int, input().split())
K -= 1
dp[K] = 0
dfs(K)

for _ in range(Q):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    print(dp[x] + dp[y])