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
doukasen = [tuple(map(int, input().split())) for _ in range(N)]
total_time = 0
for a, b in doukasen:
    total_time += a/b

harf_time = total_time/2
ans = 0
for a, b in doukasen:
    if harf_time < a/b:
        ans += harf_time * b
        exit(print(ans))
    else:
        ans += a
        harf_time -= a/b
