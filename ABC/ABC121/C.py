from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

N, M = map(int, input().split())
drink = [tuple(map(int, input().split())) for _ in range(N)]
drink.sort()
cnt = 0
ans = 0
for i in range(N):
    if cnt == M:break
    a, b = drink[i]
    if cnt + b >= M:
        ans += a*(M-cnt)
        cnt = M
    else:
        ans += a*b
        cnt += b

print(ans)

    
