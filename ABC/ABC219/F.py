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
K = int(input())
ans = 1
def dfs(x, y, seen, i):
    global ans
    print(x, y)
    if i == len(S):
        return
    if (x, y) not in seen:
        ans += 1
    seen.add((x, y))
    if S[i] == "L":
        nextx = x-1
        nexty = y
    elif S[i] == "R":
        nextx = x+1
        nexty = y
    elif S[i] == "U":
        nextx = x
        nexty = y-1
    else:
        nextx = x
        nexty = y+1
    dfs(nextx, nexty, seen, i+1)
    if (x, y) in seen:
        seen.remove((x, y))
    return
dfs(0, 0, set(), 0)
print(ans)
