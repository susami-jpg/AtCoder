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
B = [list(map(int, input().split())) for _ in range(2)]
C = [list(map(int, input().split())) for _ in range(3)]

S = 0
for i in range(2):
    S += sum(B[i])
for i in range(3):
    S += sum(C[i])
    
def calc_score(field):
    chokudai = 0
    for i in range(2):
        for j in range(3):
            if field[i][j] == field[i+1][j]:
                chokudai += B[i][j]
    
    for i in range(3):
        for j in range(2):
            if field[i][j] == field[i][j+1]:
                chokudai += C[i][j]
    return chokudai

def dfs1(field, d):
    max_score = -INF
    for i in range(3):
        for j in range(3):
            if field[i][j] == -1:
                field[i][j] = 0
                chokuko = dfs2(field, d+1)
                max_score = max(max_score, S-chokuko)
                field[i][j] = -1
    return max_score

def dfs2(field, d):
    if d == 9:
        return S - calc_score(field)
    max_score = -INF
    for i in range(3):
        for j in range(3):
            if field[i][j] == -1:
                field[i][j] = 1
                chokudai = dfs1(field, d+1)
                max_score = max(max_score, S-chokudai)
                field[i][j] = -1
    return max_score

field = [[-1] * 3 for _ in range(3)]
chokudai = dfs1(field, 0)
print(chokudai)
print(S-chokudai)

