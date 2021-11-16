from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

N, D = map(int, input().split())

A = 0
while 1:
    if D%2:
        break
    D //= 2
    A += 1

B = 0
while 1:
    if D%3:
        break
    D //= 3
    B += 1

C = 0
while 1:
    if D%5:
        break
    D //= 5
    C += 1

if D != 1:
    print(0)
    exit()

dp = [[[[0] * (C+1) for _ in range(B+1)] for _ in range(A+1)] for _ in range(N+1)]
dp[0][0][0][0] = 1
num2 = [0, 1, 0, 2, 0, 1]
num3 = [0, 0, 1, 0, 0, 1]
num5 = [0, 0, 0, 0, 1, 0]
for i in range(N):
    for a in range(A+1):
        for b in range(B+1):
            for c in range(C+1):
                if dp[i][a][b][c] == 0:continue
                cnd = dp[i][a][b][c]
             
                for k in range(6):
                    nxt_a = min(a+num2[k], A)
                    nxt_b = min(b+num3[k], B)
                    nxt_c = min(c+num5[k], C)
                    dp[i+1][nxt_a][nxt_b][nxt_c] += cnd
    
ans = dp[N][A][B][C]/pow(6, N)
print(ans)

                    
                    