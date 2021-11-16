from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt, factorial
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

A, B, K = map(int, input().split())
def combinations_count(n, r):
    return factorial(n) // (factorial(n-r) * factorial(r))

ans = ""
rest_A = A
rest_B = B
def check(a, b):
    c = combinations_count(a, b)
    return c
    
while len(ans) < A+B:
    if rest_A:
        c = check(rest_A+rest_B-1, rest_A-1)
        if c >= K:
            ans += "a"
            rest_A -= 1
        else:
            ans += "b"
            rest_B -= 1
            K -= c
    else:
        ans += "b"*rest_B
print(ans)
