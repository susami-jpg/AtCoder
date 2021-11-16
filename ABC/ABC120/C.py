from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

S = list(input())
ans = 0
while 1:
    delete = []
    prev = len(S)
    for i in S:
        if delete and delete[-1] != i:
            delete.pop()
            ans += 2
        else:
            delete.append(i)
    if prev == len(delete):
        print(ans)
        break
    S = delete

