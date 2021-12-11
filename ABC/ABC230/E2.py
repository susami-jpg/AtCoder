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
i = 1
ans = 0
# N/i - 1 < [N/i] <= N/i より、[N/i] = x とすると
# N/(x+1) < i <= N/xである。
#よって、x = [N/i]のiの最大値+1は、ni = N//x + 1となる
while i <= N:
    x = N//i
    ni = N//x + 1
    ans += x*(ni-i)
    i = ni
print(ans)
