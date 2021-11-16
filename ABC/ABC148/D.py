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
A = list(map(int, input().split()))
ans = 0
now = 1
for i in range(N):
    ans += 1
    if A[i] == now:
        now += 1
        ans -= 1
if now == 1:
    print(-1)
else:
    print(ans)
    
        