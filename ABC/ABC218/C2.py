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
s = [input() for _ in range(N)]
t = [input() for _ in range(N)]
S = [[0] * N for _ in range(N)]
T = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if s[i][j] == "#":
            S[i][j] = 1
        if t[i][j] == "#":
            T[i][j] = 1


def corner_find(A):
    li = INF
    lj = INF
    for i in range(N):
        for j in range(N):
            if A[i][j]:
                li = min(li, i)
                lj = min(lj, j)
    return li, lj

def rotate(T):
    h = len(T)
    w = len(T[0])
    new = [['.'] * h for _ in range(w)]
    for i in range(h):
        for j in range(w):
            new[w-1-j][i] = T[i][j]
    return new

def check(A, li_a, lj_a, B, li_b, lj_b):
    for i in range(N):
        for j in range(N):
            ai = li_a + i
            aj = lj_a + j
            if ai < N and aj < N:
                a = A[ai][aj]
            else:
                a = 0
            bi = li_b + i
            bj = lj_b + j
            if bi < N and bj < N:
                b = B[bi][bj]
            else:
                b = 0
            
            if a != b:
                return False
    else:
        return True

ok = False
for _ in range(4):
    li_a, lj_a = corner_find(S)
    li_b, lj_b = corner_find(T)
    ok |= check(S, li_a, lj_a, T, li_b, lj_b)
    S = rotate(S)

if ok:
    print("Yes")
else:
    print("No")
    
            
            