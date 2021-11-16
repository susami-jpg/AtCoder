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

N, M = map(int, input().split())
A = []
for _ in range(M):
    k = int(input())
    a = list(map(int, input().split()))[::-1]
    a = list(map(lambda x: x-1, a))
    A.append(a)

lastball = [[] for _ in range(N)]
stack = []
for i in range(M):
    c = A[i][-1]
    lastball[c].append(i)
    if len(lastball[c]) == 2:
        stack.append(c)

def check(c):
    for i in lastball[c]:
        A[i].pop()
        if len(A[i]):
            new_c = A[i][-1]
            lastball[new_c].append(i)
            if len(lastball[new_c]) == 2:
                new_stack.append(new_c)
cnt = 0
while stack:
    new_stack = []
    for c in stack:
        cnt += 1
        new_c = check(c)
        if new_c:
            new_stack.append(new_c)
    stack = new_stack

if cnt == N:
    print("Yes")
else:
    print("No")

"""
4 3
4
1 2 3 4
2
1 3
2
4 2
"""