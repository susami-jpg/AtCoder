from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
INF = 10**15
MOD = 10**9+7

S1 = input()
S2 = input()
S3 = input()
contest = ["ABC", "ARC", "AGC", "AHC"]
contest = set(contest)
for i in [S1, S2, S3]:
    contest.remove(i)

contest = list(contest)
print(*contest)