from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt, factorial
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

def OrLessThan(K: int, A: list) -> int:
    '配列Aの中のうち、k以下の個数と終わりの0indexを返すライブラリ'
    '-1の時は解が無い時'
    ans = bisect_right(A, K)
    return ans, (-1 if ans == 0 else ans - 1)

def OrLessThan(K: int, A: list) -> int:
    '配列Aの中のうち、k以下の個数と終わりの0indexを返すライブラリ'
    '-1の時は解が無い時'
    ans = bisect_right(A, K)
    return ans, (-1 if ans == 0 else ans - 1)

A, B, Q = map(int, input().split())
S = [int(input()) for _ in range(A)]
T = [int(input()) for _ in range(B)]
S.append(-INF)
S.append(INF)
T.append(-INF)
T.append(INF)
S.sort()
T.sort()

for _ in range(Q):
    x = int(input())
    _, ind = OrLessThan(x, S)
    A_l = S[ind]
    A_r = S[ind+1]
    _, ind = OrLessThan(x, T)
    B_l = T[ind]
    B_r = T[ind+1]

    c1 = abs(x-A_l) + abs(A_l-B_r)
    c2 = abs(x-A_r) + abs(A_r-B_l)
    c3 = abs(x-B_l) + abs(A_r-B_l)
    c4 = abs(x-B_r) + abs(A_l-B_r)
    c5 = abs(x-A_l) + abs(A_l-B_l)
    c6 = abs(x-B_l) + abs(A_l-B_l)
    c7 = abs(x-A_r) + abs(A_r-B_r)
    c8 = abs(x-B_r) + abs(A_r-B_r)
    print(min([c1, c2, c3, c4, c5, c6, c7, c8]))
    
    
