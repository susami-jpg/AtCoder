from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt, factorial
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

S = " " + input()
N = len(S)
dp = [[0] * 9 for _ in range(N)]
dp[0][0] = 1
cho = " chokudai"
for i in range(1, N):
    for j in range(9):
        dp[i][j] += dp[i-1][j]
        if S[i] == cho[j]:
            dp[i][j] += dp[i-1][j-1]
            dp[i][j] %= MOD

print(dp[-1][8])
