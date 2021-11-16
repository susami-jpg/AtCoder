from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt, factorial
from decimal import Decimal
#decimalには文字列で渡す PyPyは遅いのでPython3で提出する
#d1 = Decimal('1.1') d2 = Decimal('2.3') -> d1 + d2などの演算で浮動小数点数での誤差がなくなる(割り算もok)
INF = 10**15
MOD = 998244353

N = int(input())
S = input()
dp = [[[0] * 11 for _ in range(1 << 10)] for _ in range(N+1)]
dp[0][0][0] = 1
for i in range(N):
    for s in range(1 << 10):
        for j in range(11):
            if dp[i][s][j] == 0:continue
            nxt_contest = ord(S[i]) - 65
            #参加済みの場合
            if (s>>nxt_contest)&1:
                #最後の参加がnxt_contestの場合
                if j == nxt_contest:
                    dp[i+1][s][nxt_contest] += dp[i][s][j]
                    dp[i+1][s][nxt_contest] %= MOD
            else:
                dp[i+1][s|(1<<nxt_contest)][nxt_contest] += dp[i][s][j]
                dp[i+1][s|(1<<nxt_contest)][nxt_contest] %= MOD

            #i回目のコンテストに参加しない場合
            dp[i+1][s][j] += dp[i][s][j]
            dp[i+1][s][j] %= MOD
ans = 0
for s in range(1<<10):
    for j in range(11):
        ans += dp[N][s][j]
        ans %= MOD
#ひとつも参加していない場合を除く
ans -= 1
print(ans%MOD)
