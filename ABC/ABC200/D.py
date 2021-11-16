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
A = [0] + list(map(int, input().split()))

dp = [[[0] * 2 for _ in range(200)] for _ in range(N+1)]
dp[0][0][0] = 1
for i in range(N):
    for j in range(200):
        dp[i+1][j][0] += dp[i][j][0] 
        dp[i+1][j][1] += dp[i][j][1]
        dp[i+1][(j+A[i+1])%200][1] += dp[i][j][0]
        dp[i+1][(j+A[i+1])%200][1] += dp[i][j][1]
        dp[i+1][(j+A[i+1])%200][1] = min(dp[i+1][(j+A[i+1])%200][1], 2)
B = []
C = []
for j in range(200):
    if dp[N][j][1] > 1:
        break
else:
    print('No')
    exit()

i = N
now = j
while i > 0:
    nxtj = (j-A[i])%200
    if dp[i-1][j][1] > 0 and dp[i-1][nxtj][1] > 0:
        pass
    elif dp[i-1][j][1] == 0:
        B.append(i)
        j = nxtj
    if j == 0 and dp[i-1][j][1] == 0:
        break
    i -= 1

i = N
j = now
while i > 0:
    nxtj = (j-A[i])%200
    if dp[i-1][j][1] > 0 and dp[i-1][nxtj][1] > 0 or nxtj == 0:
        C.append(i)
        j = nxtj
    elif dp[i-1][j][1] == 0:
        C.append(i)
        j = nxtj
    if j == 0 and dp[i-1][j][1] == 0:
        break
    i -= 1
    
print('Yes')
print(len(B), *B[::-1])
print(len(C), *C[::-1])
