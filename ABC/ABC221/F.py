from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 998244353

N = int(input())
edge = [[] for _ in range(N)]
for _ in range(N-1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    edge[v].append(u)
    edge[u].append(v)

dp = [-1] * N
def dfs(v, par=-1):
    for nextv in edge[v]:
        if nextv == par:continue
        dp[nextv] = dp[v] + 1
        dfs(nextv, v)
    return

dp[0] = 0
dfs(0)
D = max(dp)
v_ind = dp.index(D)
print(dp)
dp[v_ind] = 0
dfs(v_ind)
print(dp)

D = max(dp)
mx = 0
for i in range(N):
    if dp[i] == D:
        mx += 1
print(mx)
#逆元によるnCkの高速計算
def inv(n): # MODを法とした逆元
    return pow(n, MOD-2, MOD)

fact = [1] * (mx+1) # 階乗を格納するリスト
for i in range(mx):
    fact[i+1] = fact[i] * (i+1) % MOD # 階乗を計算

def comb(n, k):
    MOD = 10**9+7
    return (fact[n] * inv(fact[n-k])) % MOD # comb(n,k) = n!/((n-k)!k!)

ans = 0
for k in range(2, mx+1):
    ans += comb(mx, k)
    ans %= MOD
print(ans)
