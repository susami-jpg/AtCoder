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

N, K = map(int, input().split())
P = [list(map(int, input().split())) for _ in range(N)]
p = [0] * N
points = []
for i in range(N):
    res = sum(P[i])
    p[i] = res
    points.append(res)
points.sort()
def More(K: int, A: list) -> int:
    '配列Aの中のうち、kより大きいものの個数と始まりの0indexを返すライブラリ'
    '-1の時は解が無い時'
    ans = bisect_right(A, K)
    l = len(A)
    return l - ans, (ans if ans <= l - 1 else -1)

for i in range(N):
    k, ind = More(p[i] + 300, points)
    if k+1 > K:
        print("No")
    else:
        print("Yes")
    
    