from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

#dp[i][j]:= i番目までの魔法でモンスターの体力をjにするときの最小の魔力合計値
H, N = map(int, input().split())
magic = [tuple(map(int, input().split())) for _ in range(N)]
dp = [[INF] * (H+1) for _ in range(N+1)]
dp[0][H] = 0
for i in range(N):
    A, B = magic[i]
    for j in range(H, -1, -1):
        dp[i+1][j] = min(dp[i+1][j], dp[i][j])
        dp[i][max(j-A, 0)] = min(dp[i][j] + B, dp[i][max(j-A, 0)])
#for row in dp:
    #print(row)
print(dp[N-1][0])
