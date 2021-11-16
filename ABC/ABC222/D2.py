from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt, factorial
from copy import copy, deepcopy
INF = 10**15
MOD = 998244353

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [[0] * 3001 for _ in range(N)]
for i in range(N):
    for j in range(3001):
        dp[i][j] += dp[i][j-1]
        dp[i][j] %= MOD
        if i == 0 and A[i] <= j <= B[i]:
            dp[i][j] += 1
        elif i != 0 and A[i] <= j <= B[i]:
            dp[i][j] += dp[i-1][j]
            dp[i][j] %= MOD
print(dp[-1][-1])

        