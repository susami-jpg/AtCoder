from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt, factorial
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

for i1 in range(H-1):
    for i2 in range(i1+1, H):
        for j1 in range(W-1):
            for j2 in range(j1+1, W):
                if A[i1][j1] + A[i2][j2] > A[i2][j1] + A[i1][j2]:
                    print("No")
                    exit()
print("Yes")
