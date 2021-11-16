from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
INF = 10**15
MOD = 10**9+7

input = stdin.readline
Q = int(input())
deq = []
hq = []
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        x = int(query[1])
        deq.append(x)
    elif query[0] == 2:
        if len(hq):
            print(heappop(hq))
        else:
            print(deq.pop(0))
    else:
        for d in deq:
            heappush(hq, d)
        deq = []