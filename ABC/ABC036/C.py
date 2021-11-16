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
A = list(int(input()) for _ in range(N))

def CC(A: list) -> list:
    '座標圧縮'
    B = {j: i for i, j in enumerate(sorted(list(set(A))))}
    return B

cc = CC(A)
for i in range(N):
    print(cc[A[i]])
    