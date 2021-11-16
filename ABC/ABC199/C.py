from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

N = int(input())
S = list(input())
Q = int(input())
flg = 0
for _ in range(Q):
    T, A, B = map(int, input().split())
    if T == 1:
        A -= 1
        B -= 1
        if flg:
            if A <= N-1:
                A += N
            else:
                A -= N
            if B <= N-1:
                B += N
            else:
                B -= N
        S[A], S[B] = S[B], S[A]
    else:
        flg = 1-flg
if flg:
    S = S[N:] + S[:N]

print("".join(S))
