from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt, factorial
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

N, A, B, C = map(int, input().split())
L = [int(input()) for _ in range(N)]

"""
def all_comb(l, i, n):
    S = []
    rest = []
    for j in range(n):
        if (i>>j)&1:
            S.append(l[j])
        else:
            rest.append(l[j])
    return S, rest

def calc_cost(l, S):
    n = len(S)
    s = sum(S)
    cost = 10*(n-1)
    cost += abs(s-l)
    return cost

ans = INF
for i1 in range(1<<N):
    a_set, rest1 = all_comb(L, i1, N)
    N2 = len(rest1)
    if N2 == 0 or len(a_set) == 0:continue
    for i2 in range(1<<N2):
        b_set, rest2 = all_comb(rest1, i2, N2)
        N3 = len(rest2)
        if N3 == 0 or len(b_set) == 0:continue
        for i3 in range(1<<N3):
            c_set, rest3 = all_comb(rest2, i3, N3)
            if len(c_set) == 0:continue
            
            cost = calc_cost(A, a_set) + calc_cost(B, b_set) + calc_cost(C, c_set)
            ans = min(ans, cost)
            
print(ans)
"""

ans = INF
for i in range(1<<(2*N)):
    a_set = []
    b_set = []
    c_set = []
    for j in range(N):
        if (i>>(2*j))&3 == 0:
            a_set.append(L[j])
        elif (i>>(2*j))&3 == 1:
            b_set.append(L[j])
        elif (i>>(2*j))&3 == 2:
            c_set.append(L[j])
    la = len(a_set)
    lb = len(b_set)
    lc = len(c_set)
    if la == 0 or lb == 0 or lc == 0:continue
    res = 0
    res += (la + lb + lc - 3) * 10
    res += abs(A - sum(a_set)) + abs(B - sum(b_set)) + abs(C - sum(c_set))
    ans = min(ans, res)
print(ans)

            
