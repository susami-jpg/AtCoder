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

#TLE
"""
setrecursionlimit(10**7)
N, Z, W = map(int, input().split())
A = list(map(int, input().split()))[::-1]
dp = dict()
#dfsは残りのカード枚数がrest枚、Xさんのカードがx、Yさんのカードがyでturnの手番である場合から初めて最適行動を獲った場合のスコア
#知りたいのはdfs(N, Z, W, 0)
def dfs(rest, x, y, turn):
    if (rest, turn, x, y) in dp:
        return dp[(rest, turn, x, y)]
    if rest == 0:
        dp[(rest, turn)] = abs(x-y)
        return abs(x-y)
    if turn == 0:
        score = -INF
        for i in range(rest-1, -1, -1):
            score = max(score, dfs(i, A[i], y, 1))
        dp[(rest, turn, x, y)] = score
        return score
    else:
        score = INF
        for i in range(rest-1, -1, -1):
            score = min(score, dfs(i, x, A[i], 0))
        dp[(rest, turn, x, y)] = score
        return score
ans = dfs(N, Z, W, 0)
print(ans)
"""

N, Z, W = map(int, input().split())
A = list(map(int, input().split()))
dp = [[0] * 2 for _ in range(N+1)]
#dp[i][p]:= i枚とり、pの手番の時の最適スコア
dp[N][0] = INF
dp[N][1] = -INF
#遷移は残りi枚の状態からi < jを満たすjについてmax or minをとる
#ただし、全てのカードを残りi枚の状態からとる場合、相手のカード(A[i-1] or 初期カード) とA[N-1](最後のカード)のabsとなる
for i in range(N-1, -1, -1):
    #Xの手番
    #相手のカード
    if i-1 < 0:
        y_card = W
    else:
        y_card = A[i-1]
    #全てとる場合で初期化
    dp[i][0] = abs(y_card-A[N-1])
    for j in range(i+1, N+1):
        dp[i][0] = max(dp[i][0], dp[j][1])
    
    #Yの手番
    #相手のカード
    if i-1 < 0:
        x_card = Z
    else:
        x_card = A[i-1]
    #全てとる場合で初期化
    dp[i][1] = abs(x_card-A[N-1])
    for j in range(i+1, N+1):
        dp[i][1] = min(dp[i][1], dp[j][0])
print(dp[0][0])
