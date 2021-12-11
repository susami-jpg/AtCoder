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

H, W, N = map(int, input().split())
numbers = []
for i in range(N):
    r, c, a = map(int, input().split())
    numbers.append((a, r, c, i))
ans = [-1] * N
numbers.sort(reverse=True)
row = [-INF] * (H+1)
column = [-INF] * (W+1)
prev = -1
stack = []
for a, r, c, i in numbers:
    update = False
    if prev != a:
        update = True
    if update:
        for r1, c1, i1 in stack:
            row[r1] = max(row[r1], ans[i1])
            column[c1] = max(column[c1], ans[i1])
        stack = []
    ans[i] = max(row[r] + 1, column[c] + 1, 0)
    stack.append((r, c, i))
    prev = a

print(*ans)

            