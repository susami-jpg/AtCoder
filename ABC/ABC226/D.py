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

# Euclidean Algorithm
def gcd(m, n):
    if m == 0:
        return n
    elif n == 0:
        return m
    r = m % n
    return gcd(n, r) if r else n

N = int(input())
plots = [tuple(map(int, input().split())) for _ in range(N)]
magic = defaultdict(int)
ans = 0
for i in range(N-1):
    for j in range(i+1, N):
        dx = plots[i][0] - plots[j][0]
        dy = plots[i][1] - plots[j][1]
        g = gcd(dx, dy)
        if magic[(dx//g, dy//g)] == 0:
            ans += 1
            magic[(dx//g, dy//g)] = 1
            
        if magic[(-dx//g, -dy//g)] == 0:
            ans += 1
            magic[(-dx//g, -dy//g)] = 1
            
#for key, val in magic.items():
    #print(key)
print(ans)
