from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt, factorial
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

N, Q = map(int, input().split())
front = [-1] * N
back = [-1] * N
for _ in range(Q):
    query = list(map(int, input().split()))
    if len(query) == 3:
        q, x, y = query
        x -= 1
        y -= 1
        if q == 1:
            back[x] = y
            front[y] = x
        else:
            back[x] = -1
            front[y] = -1
    else:
        x = query[1]
        x -= 1
        while front[x] != -1:
            x = front[x]
        ans = [x+1]
        while back[x] != -1:
            x = back[x]
            ans.append(x+1)
        print(len(ans), *ans)
        
