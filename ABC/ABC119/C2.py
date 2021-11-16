from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt, factorial
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

setrecursionlimit(10**7)
N, A, B, C = map(int, input().split())
L = [int(input()) for _ in range(N)]

def dfs(v, d):
    res = INF
    if d == N:
        return calc(v)
    for nextv in range(4):
        v[d] = nextv
        res = min(res, dfs(v, d+1))
    return res

def calc(v):
    a_set = []
    b_set = []
    c_set = []
    for i in range(N):
        if v[i] == 0:
            a_set.append(L[i])
        elif v[i] == 1:
            b_set.append(L[i])
        elif v[i] == 2:
            c_set.append(L[i])
    la = len(a_set)
    lb = len(b_set)
    lc = len(c_set)
    if la == 0 or lb == 0 or lc == 0:
        return INF
    res = 0
    res += (la + lb + lc - 3) * 10
    res += abs(A - sum(a_set))
    res += abs(B - sum(b_set))
    res += abs(C - sum(c_set))
    return res

ans = INF
ans = min(ans, dfs([-1] * N, 0))
print(ans)

    
