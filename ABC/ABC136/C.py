from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

N = int(input())
H = list(map(int, input().split()))
max_h = H[-1]
for i in range(N-2, -1, -1):
    if H[i]-1 > max_h:
        print('No')
        exit()
    elif H[i]-1 == max_h:
        H[i] -= 1
    max_h = H[i]
print('Yes')