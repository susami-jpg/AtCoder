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

def f(a, b):
    return 4*a*b + 3*a + 3*b

N = int(input())
S = list(map(int, input().split()))
ans = 0
for s in S:
    ok = False
    for a in range(1, 600):
        for b in range(1, 600):
            if f(a, b) == s:
                ok = True
    if not ok:
        ans += 1
print(ans)
