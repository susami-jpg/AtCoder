from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

N = int(input())
S = input()
X = input()
dp = [[False] * 7 for _ in range(N+1)]
dp[N][0] = True

for i in range(N-1, -1, -1):
    for j in range(7):
        if X[i] == 'T':
            dp[i][j] |= dp[i+1][(j*10 + int(S[i]))%7]
            dp[i][j] |= dp[i+1][(j*10)%7]
        else:
            if dp[i+1][(j*10 + int(S[i]))%7] and dp[i+1][(j*10)%7]:
                dp[i][j] = True

if dp[0][0]:
    print('Takahashi')
else:
    print('Aoki')
    