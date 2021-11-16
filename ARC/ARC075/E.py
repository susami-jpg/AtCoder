from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

N, K = map(int, input().split())
A = [int(input()) for _ in range(N)]
dp = [0] * (N+1)
acc_sum = 0
for i in range(N):
    dp[i] = acc_sum - K*i
    acc_sum += A[i]
dp[-1] = acc_sum - K*N

