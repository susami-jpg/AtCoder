from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

N = int(input())
X, Y = map(int, input().split())
bento = [tuple(map(int, input().split())) for _ in range(N)]
dp = [[[INF] * (Y+1) for _ in range(X+1)] for _ in range(N+1)]
dp[0][0][0] = 0
for i in range(N):
    A, B = bento[i]
    for j in range(X+1):
        for k in range(Y+1):
            dp[i+1][j][k] = min(dp[i+1][j][k], dp[i][j][k])
            if j+A > X:
                nxtj = X
            else:
                nxtj = j+A
            if k+B > Y:
                nxtk = Y
            else:
                nxtk = k+B
            dp[i+1][nxtj][nxtk] = min(dp[i+1][nxtj][nxtk], dp[i][j][k] + 1)

if dp[-1][X][Y] == INF:
    print(-1)
else:
    print(dp[-1][X][Y])
    