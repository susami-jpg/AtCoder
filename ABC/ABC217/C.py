from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
INF = 10**15
MOD = 10**9+7

N = int(input())
P = list(map(int, input().split()))

Q = [0] * N
for ind, val in enumerate(P):
    val -= 1
    ind += 1
    Q[val] = ind
print(*Q)

