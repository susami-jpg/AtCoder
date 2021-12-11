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

N, X = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
X -= 1
deq = deque()
deq.append(X)
seen = [0] * N
while deq:
    v = deq.popleft()
    seen[v] = 1
    ans += 1
    if seen[A[v]-1] == 0:
        deq.append(A[v]-1)
print(ans)
