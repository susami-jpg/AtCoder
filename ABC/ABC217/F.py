from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
INF = 10**15
MOD = 998244353

N, M = map(int, input().split())
friends = [[0] * 4*N for _ in range(4*N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    friends[a][b] = 1
    friends[b][a] = 1

#dp[i][j]:= i,i+1,i+2,,,i+2*j-1人の2*j人の生徒をj組の組み合わせにする通り数
dp = [[0] * (N+1) for _ in range(4*N)]
#初期化: 生徒iから数えて0組を取り除く場合の数を1とする
for i in range(4*N):
    dp[i][0] = 1

#逆元によるnCkの高速計算
def inv(n): # MODを法とした逆元
    return pow(n, MOD-2, MOD)

mx = 300
fact = [1] * (mx+1) # 階乗を格納するリスト
for i in range(mx):
    fact[i+1] = fact[i] * (i+1) % MOD # 階乗を計算

def comb(n, k):
    return (fact[n] * inv(fact[n-k]) * inv(fact[k])) % MOD # comb(n,k) = n!/((n-k)!k!)


for j in range(1, N+1):
    for i in range(2*N):
        for k in range(1, j+1):
            dp[i][j] += ((dp[i+1][k-1] * dp[i+2*k][j-k])%MOD) * friends[i][i+2*k-1] * comb(j, k)
            dp[i][j] %= MOD

print(dp[0][N])


            
            

