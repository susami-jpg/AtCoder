from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
INF = 10**15
MOD = 10**9+7

poll = defaultdict(int)
max_p = 0
N = int(input())
name = set()
for _ in range(N):
    s = input()
    name.add(s)
    poll[s] += 1
    max_p = max(max_p, poll[s])

name = list(name)
name.sort()
for s in name:
    if poll[s] == max_p:
        print(s)
