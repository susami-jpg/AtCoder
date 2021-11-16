from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

N, K = map(int, input().split())
game = [0] + [int(input()) for _ in range(N)]
acc_game = list(accumulate(game))
if sum(game) == K:
    print(1)
    exit()
dp = [[INF] * (N+1) for _ in range(N+1)]
dp[0][0] = 0
for i in range(1, N+1):
    for j in range(i+1):
        dp[i][j] = dp[i-1][j]
        if j-1 >= 0:
            if acc_game[i-1] == 0:
                v_cnt = 1
            else:
                v_cnt = (dp[i-1][j-1] * acc_game[i]) // acc_game[i-1] + 1
            if v_cnt - dp[i-1][j-1] > game[i]:continue
            dp[i][j] = min(dp[i][j], v_cnt)

def OrLessThan(K: int, A: list) -> int:
    '配列Aの中のうち、k以下の個数と終わりの0indexを返すライブラリ'
    '-1の時は解が無い時'
    ans = bisect_right(A, K)
    return ans, (-1 if ans == 0 else ans - 1)

_, ans = OrLessThan(K, dp[N])
print(ans)

    

