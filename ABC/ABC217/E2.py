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

Q = int(input())
sorted = []
unsorted = deque()
for _ in range(Q):
    query = list(map(int, input().split()))
    if len(query) == 2:
        x = query[1]
        unsorted.append(x)
    else:
        q = query[0]
        if q == 2:
            if sorted:
                print(heappop(sorted))
            else:
                print(unsorted.popleft())
        else:
            for d in unsorted:
                heappush(sorted, d)
            unsorted = deque()

            
            
            