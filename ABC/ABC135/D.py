from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

S = input()[::-1]
S += "0"
N = len(S)
dp = [[0] * 13 for _ in range(N)]
P = [0] * N
for i in range(N):
    P[i] = pow(10, i, 13)
if S[0] != "?":
    dp[0][int(S[0])] = 1
else:
    for j in range(10):
        dp[0][j] = 1
for i in range(N-1):
    for j in range(13):
        if S[i+1] != "?":
            num = int(S[i+1])
            nxtj = (j+num*P[i+1])%13
            dp[i+1][nxtj] += dp[i][j]
            dp[i+1][nxtj] %= MOD
        else:
            for k in range(10):
                nxtj = (j+k*P[i+1])%13
                dp[i+1][nxtj] += dp[i][j]
                dp[i+1][nxtj] %= MOD

print(dp[-1][5])

                