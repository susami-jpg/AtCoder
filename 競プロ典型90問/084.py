from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
INF = 10**15
MOD = 10**9+7

N = int(input())
S = input()

ans = 0
#dp[i]: = i以前に自分と異なる記号が出た最も右の1index
dp = [0] * N
for i in range(1, N):
    if S[i] == S[i-1]:
        dp[i] = dp[i-1]
    else:
        dp[i] = i

ans = sum(dp)
print(ans)



