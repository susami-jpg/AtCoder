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
if N == 0:
    exit(print(0))
if N%2:
    N -= 1
    s0 = 1
else:
    s0 = 0

s_even = 0
s_odd = 0
def make_s_even(bit):
    res = 0
    for j in range(bit.bit_length()):
        if (bit>>j)&1:
            res |= 1<<(2*j)
    return res

def make_s_odd(bit):
    res = 0
    for j in range(bit.bit_length()):
        if (bit>>j)&1:
            res |= 1<<(2*j+1)
    return res

for i in range(1<<20):
    s_even = make_s_even(i)
    s_odd = s_even - N
    for j in range(60):
        if (s_odd>>(2*j))&1:break
    else:
        ans = s_even|s_odd|s0
        exit(print(bin(ans)[2:]))
            