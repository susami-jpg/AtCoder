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
cost = [[INF] * N for _ in range(N)]
for _ in range(M):
    s, t, d = map(int, input().split())
    cost[s][t] = d

#dp[S][v]:= 集合Sをvが最終到達地点となるように訪問する最短時間
dp = [[-1] * N for _ in range(1<<N)]

def dfs(S, v):
    #探索済みの場合
    if dp[S][v] != -1:
        return dp[S][v]
    #スタート地点の場合
    if S == 0:
        #スタート地点が0(適切)の場合0
        if v == 0:
            dp[S][v] = 0
            return 0
        #スタート地点が適切でない場合
        else:
            dp[S][v] = INF
            return INF
    #現在地点が訪問済み集合に含まれていないとき
    if S&(1<<v) == 0:
        dp[S][v] = INF
        return INF
    
    #最短時間の探索
    res = INF
    for prev in range(N):
        res = min(res, dfs(S^(1<<v), prev) + cost[prev][v])
    dp[S][v] = res
    return res

ans = dfs((1<<N)-1, 0)
if ans == INF:
    print(-1)
else:
    print(ans)
    

        


