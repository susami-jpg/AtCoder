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
print(0, flush=True)
s = input()
if s == "Vacant":
    exit()
elif s == "Male":
    man = 0
    woman = 1
else:
    man = 1
    woman = 0

print(N-1, flush=True)
s = input()
if s == "Vacant":
    exit()

left = 0
right = N-1
for _ in range(19):
    mid = (left+right)//2
    print(mid, flush=True)
    s = input()
    if s == "Vacant":
        exit()
    elif s == "Male":
        if mid%2 == man:
            left = mid
        else:
            right = mid
    else:
        if mid%2 == woman:
            left = mid
        else:
            right = mid
