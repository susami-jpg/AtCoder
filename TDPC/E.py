from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

D = int(input())
N = [0] + list(map(int, list(input())))
n = len(N)
dp = [[[0] * D for _ in range(2)] for _ in range(n)]
dp[0][0][0] = 1

for i in range(n-1):
    for smaller in range(2):
        for j in range(D):
            if dp[i][smaller][j] == 0:continue
            if smaller:
                for nxt in range(10):
                    dp[i+1][1][(j+nxt)%D] += dp[i][smaller][j]
                    dp[i+1][1][(j+nxt)%D] %= MOD
            else:
                ceil_num = N[i+1]
                for nxt in range(ceil_num):
                    dp[i+1][1][(j+nxt)%D] += dp[i][smaller][j]
                    dp[i+1][1][(j+nxt)%D] %= MOD
                dp[i+1][0][(j+ceil_num)%D] += dp[i][smaller][j]
                dp[i+1][0][(j+ceil_num)%D] %= MOD

ans = dp[-1][0][0] + dp[-1][1][0] - 1
ans %= MOD
print(ans)
