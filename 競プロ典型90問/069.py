from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right
from math import sqrt
INF = 10**15
MOD = 10**9+7

N, K = map(int, input().split())
ans = K%MOD
if N == 1:
    print(ans)
else:
    ans *= (K-1)
    ans %= MOD
    ans *= pow(K-2, N-2, MOD)
    print(ans%MOD)

