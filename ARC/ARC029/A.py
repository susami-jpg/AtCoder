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
T = [0] + [int(input()) for _ in range(N)]
S = sum(T)
Sh = S//2

dp = [[False] * 300 for _ in range(N+1)]
dp[0][0] = True

for i in range(1, N+1):
    for j in range(300):
        dp[i][j] |= dp[i-1][j]
        if j-T[i] >= 0:
            dp[i][j] |= dp[i-1][j-T[i]]

cnd = [ind for ind, t in enumerate(dp[-1]) if t]
cnd = [-INF] + cnd + [INF]

def OrLessThan(K: int, A: list) -> int:
    '配列Aの中のうち、k以下の個数と終わりの0indexを返すライブラリ'
    '-1の時は解が無い時'
    ans = bisect_right(A, K)
    return ans, (-1 if ans == 0 else ans - 1)

_, ind = OrLessThan(Sh, cnd)
ans = min(max(cnd[ind], abs(S-cnd[ind])), max(abs(S-cnd[ind+1]), cnd[ind+1]))
print(ans)
