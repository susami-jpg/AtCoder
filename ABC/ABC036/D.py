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
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append(b)
    edge[b].append(a)

dp = [[-1] * 2 for _ in range(N)]

def dfs(v, par=-1):
    if dp[v] != [-1, -1]:
        return dp[v]
    c0 = 1
    c1 = 1
    for nextv in edge[v]:
        if nextv == par:continue
        child0, child1 = dfs(nextv, v)
        c0 *= (child0 + child1)
        c1 *= child0
        c0 %= MOD
        c1 %= MOD
    dp[v] = [c0, c1]
    return dp[v]

dfs(0)
print(sum(dp[0])%MOD)
