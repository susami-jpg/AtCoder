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
A = []
B = []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
li = 0
lx = 0
ri = N-1
rx = 0
ans = 0
while li != ri:
    l_time = (A[li] - lx)/B[li]
    r_time = (A[ri] - rx)/B[ri]
    if l_time < r_time:
        ans += A[li] - lx
        li += 1
        lx = 0
        rx += l_time * B[ri]
    else:
        ri -= 1
        rx = 0
        ans += r_time * B[li]
        lx += r_time * B[li]

ans += (A[li] - lx - rx)/2
print(ans)
