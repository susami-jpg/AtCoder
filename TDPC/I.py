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
MOD = 10**9+7

s = input()
N = len(s) + 1
ok = [[False] * N for _ in range(N)]
dp = [0] * N
for i in range(N):
    ok[i][i] = True

for diff in range(1, N):
    for i in range(N-diff):
        j = i + diff
        for k in range(i+1, j-1):
            ok[i][j] |= ok[i][k] & ok[k][j]
            if s[i] == "i" and s[k] == "w" and s[j-1] == "i":
                ok[i][j] |= ok[i+1][k] & ok[k+1][j-1]
    

for r in range(1, N):
    dp[r] = max(dp[r], dp[r-1])
    for l in range(r):
        if ok[l][r]:
            dp[r] = max(dp[r], dp[l] + (r-l)//3)
print(dp[-1])


