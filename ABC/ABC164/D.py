from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 2019

S = list(map(int, list(input())))[::-1]
N = len(S)
A = [0] * N
for i in range(N):
    A[i] = (S[i] * pow(10, i, MOD))%MOD

A = [0] + A
acc = [0] * (N+1)
for i in range(1, N+1):
    acc[i] += acc[i-1] + A[i]
    acc[i] %= MOD

ans = 0
for key, val in Counter(acc).items():
    ans += val*(val-1)//2
print(ans)
