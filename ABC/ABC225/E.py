from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt, factorial
from copy import copy, deepcopy
from decimal import Decimal
#decimalには文字列で渡す
#d = Decimal('1.1')
INF = 10**15
MOD = 10**9+7

N = int(input())
rec = []
for _ in range(N):
    x, y = map(int, input().split())
    rec.append((Decimal(str(y-1)) / Decimal(str(x)), x, y))

rec.sort(reverse=True)
ans = 0
prev = None
for d, x, y in rec:
    #print(left, x, y)
    if prev == None:
        ans += 1
        prev = (x, y)
    else:
        px, py = prev
        if y*px <= (py-1)*(x-1):
            ans += 1
            prev = (x, y)

print(ans)
