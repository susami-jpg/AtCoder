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
N, M, K = map(int, input().split())
A = list(map(int, input().split()))
A = list(map(lambda x: x-1, A))

edge = [[] for _ in range(N)]
for i in range(N-1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    edge[u].append((v, i))
    edge[v].append((u, i))
    
    
def dfs(v, g, par=-1):
    if v == g:return
    for nextv, id in edge[v]:
        if nextv == par:continue
        #if prev[nextv] != [-1, -1]:continue
        prev[nextv] = [v, id]
        dfs(nextv, g, v)
    return

edge_cnt = [0] * (N-1)
for i in range(M-1):
    prev = [[-1, -1] for _ in range(N)]
    dfs(A[i], A[i+1], -1)
    now = A[i+1]
    while now != A[i]:
        before, used_edge = prev[now]
        edge_cnt[used_edge] += 1
        now = before
#print(edge_cnt)
S = sum(edge_cnt)
if S+K < 0 or (S+K)%2:
    exit(print(0))
else:
    R = (S+K)//2
    dp = [[0] * (R+1) for _ in range(N)]
    dp[0][0] = 1
    for i in range(N-1):
        for j in range(R+1):
            if dp[i][j] == 0:continue
            dp[i+1][j] += dp[i][j]
            dp[i+1][j] %= MOD
            if j + edge_cnt[i] <= R:
                dp[i+1][j+edge_cnt[i]] += dp[i][j]
                dp[i+1][j+edge_cnt[i]] %= MOD
    #for row in dp:
        #print(row)
    print(dp[-1][R])
    
        

