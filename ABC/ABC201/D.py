from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

H, W = map(int, input().split())
A = []
for _ in range(H):
    cin = list(input())
    new = []
    for c in cin:
        if c == "+":
            new.append(1)
        else:
            new.append(-1)
    A.append(new)
    
dp = [[0] * W for _ in range(H)]
for i in range(H-1, -1, -1):
    for j in range(W-1, -1, -1):
        if i == H-1 and j == W-1:continue
        if (i+j)%2:
            p = 1
        else:
            p = 0
            
        if p == 0:
            if i == H-1:
                dp[i][j] = dp[i][j+1] + A[i][j+1]
            elif j == W-1:
                dp[i][j] = dp[i+1][j] + A[i+1][j]
            else:
                dp[i][j] = max(dp[i+1][j] + A[i+1][j], dp[i][j+1] + A[i][j+1])
        else:
            if i == H-1:
                dp[i][j] = dp[i][j+1] - A[i][j+1]
            elif j == W-1:
                dp[i][j] = dp[i+1][j] - A[i+1][j]
            else:
                dp[i][j] = min(dp[i+1][j] - A[i+1][j], dp[i][j+1] - A[i][j+1])
    
if dp[0][0] > 0:
    print("Takahashi")
elif dp[0][0] < 0:
    print("Aoki")
else:
    print("Draw")
    
