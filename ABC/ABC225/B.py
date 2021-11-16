from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt, factorial
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

N = int(input())
edge_cnt = [0] * N
for _ in range(N-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edge_cnt[a] += 1
    edge_cnt[b] += 1

if N-1 in edge_cnt:
    print('Yes')
else:
    print("No")