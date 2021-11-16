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
sug = [[] for _ in range(N)]
for i in range(N):
    a = int(input())
    for _ in range(a):
        x, y = map(int, input().split())
        x -= 1
        sug[i].append((x, y))

ans = 0
for i in range(1 << N):
    cnt = 0
    for j in range(N):
        if (i>>j)&1:
            cnt += 1
            for x, y in sug[j]:
                if y == 1 and (i>>x)&1 == 0:
                    break
                if y == 0 and (i>>x)&1 == 1:
                    break
            else:
                continue
            break
    else:
        ans = max(ans, cnt)
print(ans)

    