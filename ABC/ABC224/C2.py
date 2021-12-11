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
points = [tuple(map(int, input().split())) for _ in range(N)]
ans = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            x1 = points[j][0] - points[i][0]
            y1 = points[j][1] - points[i][1]
            x2 = points[k][0] - points[i][0]
            y2 = points[k][1] - points[i][1]
            if x1*y2 - x2*y1 != 0:
                ans += 1
print(ans)

        