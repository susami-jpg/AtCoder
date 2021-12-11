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

setrecursionlimit(10**7)
A = [list(map(int, input().split())) for _ in range(4)]
town = 0
for i in range(4):
    for j in range(4):
        if A[i][j]:
            nj = i*4+j
            town |= (1<<nj)

def find(x):
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

def unite(x, y):
    x = find(x)
    y = find(y)
    if x == y:return
    par[x] += par[y]
    par[y] = x
    return

ans = 0
for S in range(1<<16):
    if (S&town) != town:continue
    field = [[0] * 6 for _ in range(6)]
    for i in range(4):
        for j in range(4):
            nj = i*4+j
            if (S>>nj)&1:
                field[i+1][j+1] = 1
    par = [-1] * 36
    for i in range(6):
        for j in range(6):
            if i+1 < 6 and field[i][j] == field[i+1][j]:
                unite(i*6+j, i*6+j+6)
            if j+1 < 6 and field[i][j] == field[i][j+1]:
                unite(i*6+j, i*6+j+1)
    
    cnt = 0
    for i in range(36):
        if i == find(i):
            cnt += 1
    if cnt == 2:
        ans += 1
print(ans)
