from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

ans = 0
S = list(input())

def check(key):
    for i, c in enumerate(S):
        i
        if c == "o" and (str(i) not in key):
            return False
        if c == "x" and (str(i) in key):
            return False
    else:
        return True

for key in range(10000):
    key = list(str(key))
    key = ["0"] * (4-len(key)) + key
    if check(key):
        ans += 1

print(ans)
