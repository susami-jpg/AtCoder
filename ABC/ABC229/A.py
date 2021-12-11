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

S = [input() for _ in range(2)]
s1 = S[0][0]
s2 = S[0][1]
s3 = S[1][0]
s4 = S[1][1]

if s1 == s2 == s3 == s4:
    print("Yes")
elif s1 == s4 and s2 == s3:
    print("No")
else:
    print("Yes")
    