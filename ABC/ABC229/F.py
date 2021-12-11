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

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
B = [B[-1]] + B
B.pop()

ans = INF
for si in range(2):
    dp = [[INF] * 2 for _ in range(N+1)]
    dp[0][si] = 0
    for v in range(1, N+1):
        for c in range(2):
            for pc in range(2):
                cost = 0
                #現在のnodeを白で塗る場合0-vの辺は落とす必要がある
                if c == 0:
                    cost += A[v-1]
                #現在のnodeが前のnodeと同じ色の場合、(v-1)-vの辺は落とす必要がある
                if c == pc:
                    cost += B[v-1]
                dp[v][c] = min(dp[v][c], dp[v-1][pc]+cost)
    ans = min(ans, dp[N][si])
print(ans)


            
