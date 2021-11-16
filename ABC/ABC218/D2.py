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

N = int(input())
plots = [tuple(map(int, input().split())) for _ in range(N)]
plots_set = set(plots)
ans = 0
for i in range(N):
    for j in range(N):
        xi, yi = plots[i]
        xj, yj = plots[j]
        if xi >= xj or yi <= yj:continue
        p1 = (xi, yj)
        p2 = (xj, yi)
        if p1 in plots_set and p2 in plots_set:
            ans += 1
print(ans)
