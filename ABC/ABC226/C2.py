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
T = [-1] * (N+1)
K = [-1] * (N+1)
A = [-1] * (N+1)
for i in range(N):
    inp = list(map(int, input().split()))
    t, k, a = inp[0], inp[1], inp[2:]
    T[i+1] = t
    K[i+1] = k
    A[i+1] = a

need = [False] * (N+1)
need[N] = True
for i in range(N, 0, -1):
    if need[i]:
        for j in A[i]:
            need[j] = True

ans = sum([T[i] for i in range(N+1) if need[i]])
print(ans)
