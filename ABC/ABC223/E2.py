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

def ceil(n, m):
    return - (-n // m)

X, Y, A, B, C = map(int, input().split())
def canInclude3(x, y, a, b, c):
    ok = False
    nxty = y - ceil(a, x)
    if nxty > 0:
        ok |= canInclude2(x, nxty, b, c)
    nxtx = x - ceil(a, y)
    if nxtx > 0:
        ok |= canInclude2(nxtx, y, b, c)
    return ok

def canInclude2(x, y, a, b):
    ok = False
    nxty = y - ceil(a, x)
    if nxty > 0:
        ok |= canInclude(x, nxty, b)
    nxtx = x - ceil(a, y)
    if nxtx > 0:
        ok |= canInclude(nxtx, y, b)
    return ok

def canInclude(x, y, a):
    if x * y >= a:
        return True
    else:
        return False

ans = False
ans |= canInclude3(X, Y, A, B, C)
ans |= canInclude3(X, Y, B, C, A)
ans |= canInclude3(X, Y, C, B, A)
ans |= canInclude3(X, Y, A, C, B)
ans |= canInclude3(X, Y, B, A, C)
ans |= canInclude3(X, Y, C, A, B)
if ans:
    print("Yes")
else:
    print("No")
    

