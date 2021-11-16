from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt, factorial
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

N = int(input())
T = list(map(int, input().split()))
S = sum(T)
S_harf = S/2

dp = [[False] * (10**5+1) for _ in range(N+1)]
dp[0][0] = True
for i in range(1, N+1):
    for j in range(10**5+1):
        dp[i][j] |= dp[i-1][j]
        if j-T[i-1] >= 0:
            dp[i][j] |= dp[i-1][j-T[i-1]]

cnd = [-INF] + [i for i, val in enumerate(dp[-1]) if val] + [INF]
def OrLessThan(K: int, A: list) -> int:
    '配列Aの中のうち、k以下の個数と終わりの0indexを返すライブラリ'
    '-1の時は解が無い時'
    ans = bisect_right(A, K)
    return ans, (-1 if ans == 0 else ans - 1)

_, ind = OrLessThan(S_harf, cnd)
cnd1 = cnd[ind]
cnd2 = cnd[ind+1]
ans = min(max(cnd1, S-cnd1), max(cnd2, S-cnd2))
print(ans)
