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
A = list(map(int, input().split()))
ABS = []
minus = 0
for i in range(N):
    ABS.append(abs(A[i]))
    if A[i] < 0:
        minus += 1
    
if minus%2:
    ABS.sort()
    S = sum(ABS[1:]) - ABS[0]
    print(S)
else:
    print(sum(ABS))
    
