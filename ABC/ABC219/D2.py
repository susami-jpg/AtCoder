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

N = int(input())
X, Y = map(int, input().split())
lunch_box = [tuple(map(int, input().split())) for _ in range(N)]
dp = [[[INF] * (Y+1) for _ in range(X+1)] for _ in range(N+1)]
dp[0][0][0] = 0
for i in range(N):
    a, b = lunch_box[i]
    for j in range(X+1):
        for k in range(Y+1):
            if dp[i][j][k] == INF:continue
            dp[i+1][j][k] = min(dp[i+1][j][k], dp[i][j][k])
            nxt_j = min(j+a, X)
            nxt_k = min(k+b, Y)
            dp[i+1][nxt_j][nxt_k] = min(dp[i+1][nxt_j][nxt_k], dp[i][j][k] + 1)

if dp[N][X][Y] == INF:
    print(-1)
else:
    print(dp[N][X][Y])
    