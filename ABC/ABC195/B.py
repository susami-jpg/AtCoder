from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

A, B, W = map(int, input().split())
W *= 1000
max_ans = 0
min_ans = INF
for k in range(W//B, W//A + 1):
    if A*k <= W <= B*k:
        max_ans = max(max_ans, k)
        min_ans = min(min_ans, k)

if max_ans < min_ans:
    print('UNSATISFIABLE')
else:
    print(min_ans, max_ans)
    
    