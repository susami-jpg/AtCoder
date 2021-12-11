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

N = list(map(int, list(input())))
ans = 0
n = len(N)
for i in range(1<<n):
    c1 = []
    c2 = []
    for j in range(n):
        if (i>>j)&1:
            c1.append(N[j])
        else:
            c2.append(N[j])
    if len(c1) == 0 or len(c2) == 0:continue
    c1.sort(reverse=True)
    c2.sort(reverse=True)
    if c1[0] == 0 or c2[0] == 0:continue
    ans = max(ans, int("".join(list(map(str, c1)))) * int("".join(list(map(str, c2)))))
print(ans)
