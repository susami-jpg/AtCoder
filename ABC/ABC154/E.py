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
K = int(input())
N = [0] + list(map(int, list(str(N))))
L = len(N)
dp = [[[0] * (K+1) for _ in range(2)] for _ in range(L)]
dp[0][0][0] = 1
for i in range(L-1):
    for j in range(2):
        for k in range(K+1):
            ceil = N[i+1]
            pwd = dp[i][j][k]
            if j:
                dp[i+1][j][k] += pwd
                if k+1 <= K:
                    dp[i+1][j][k+1] += pwd*9
            else:
                if ceil == 0:
                    dp[i+1][0][k] += pwd
                else:
                    dp[i+1][1][k] += pwd
                    if k+1 <= K:
                        dp[i+1][1][k+1] += pwd*(ceil-1)
                        dp[i+1][0][k+1] += pwd

print(dp[-1][0][K] + dp[-1][1][K])
