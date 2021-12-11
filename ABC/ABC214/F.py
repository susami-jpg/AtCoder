from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt, factorial
from decimal import Decimal
#decimalには文字列で渡す PyPyは遅いのでPython3で提出する
#d1 = Decimal('1.1') d2 = Decimal('2.3') -> d1 + d2などの演算で浮動小数点数での誤差がなくなる(割り算もok)
INF = 10**18
MOD = 10**9+7
setrecursionlimit(10**7)

#二つ前からの状態から見るので番兵を入れておく
S = " 　" + input()
N = len(S)
prev = [-1] * 26
dp = [0] * N
acc_dp = [0] * N
#空文字一つ目(dp[0])は1通り
#空文字二つ目(dp[1])はすでに空文字を使ったので0通りとして初期化("  "からできる部分列は" "のみ)
dp[0] = acc_dp[0] = acc_dp[1] = 1
for i in range(2, N):
    j = prev[ord(S[i])-97]        
    left = 0
    #隣り合うところは使えない条件なのでS[j-1]を使うのもok(S[j-1]を使った場合S[j]は使えないため)
    if j-2 >= 0:
        left = acc_dp[j-2]
    right = acc_dp[i-2]
    dp[i] = right - left
    dp[i] %= MOD
    acc_dp[i] = acc_dp[i-1] + dp[i]
    acc_dp[i] %= MOD
    prev[ord(S[i])-97] = i

print((acc_dp[N-1]-1)%MOD)

