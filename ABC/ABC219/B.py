from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

s1 = input()
s2 = input()
s3 = input()
T = list(map(int, list(input())))
ans = []
for i in T:
    if i == 1:
        ans.append(s1)
    elif i == 2:
        ans.append(s2)
    else:
        ans.append(s3)
print("".join(ans))

        