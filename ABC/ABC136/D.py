from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

S = input()
N = len(S)
ans = [0] * N
rec = [0] * N
r = 0
prev_r = 0
for i in range(N):
    if S[i] == "L":
        rec[i] = prev_r
    else:
        prev_r = i

prev_l = N-1
for i in range(N-1, -1, -1):
    if S[i] == "R":
        rec[i] = prev_l
    else:
        prev_l = i       

for i in range(N):
    diff = abs(rec[i]-i)
    if S[i] == "R":
        if diff%2:
            ans[rec[i]-1] += 1
        else:
            ans[rec[i]] += 1
    else:
        if diff%2:
            ans[rec[i]+1] += 1
        else:
            ans[rec[i]] += 1

print(*ans)

    
