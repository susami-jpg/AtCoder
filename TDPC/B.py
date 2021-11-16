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

a, b = map(int, input().split())
A = [0] + list(map(int, input().split()))[::-1]
B = [0] + list(map(int, input().split()))[::-1]
dp = [[0] * (b+1) for _ in range(a+1)]
for i in range(a+1):
    for j in range(b+1):
        if i == j == 0:continue
        c = -INF
        if i-1 >= 0:
            c = max(-dp[i-1][j] + A[i], c)
        if j-1 >= 0:
            c = max(-dp[i][j-1] + B[j], c)
        dp[i][j] = c
S = sum(A) + sum(B)  
print((S+dp[a][b])//2)
