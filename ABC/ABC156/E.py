from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

N, K = map(int, input().split())
#逆元によるnCkの高速計算
def inv(n): # MODを法とした逆元
    MOD = 10**9+7
    return pow(n, MOD-2, MOD)

MOD = 10**9+7
mx = 2*10**5
fact = [1] * (mx+1) # 階乗を格納するリスト
for i in range(mx):
    fact[i+1] = fact[i] * (i+1) % MOD # 階乗を計算

def comb(n, k):
    MOD = 10**9+7
    return (fact[n] * inv(fact[n-k]) * inv(fact[k])) % MOD # comb(n,k) = n!/((n-k)!k!)

ans = 0
for k in range(min(K+1, N)):
    ans += (comb(N, k) * comb(N-1, k))%MOD
    ans %= MOD
print(ans)
    
    