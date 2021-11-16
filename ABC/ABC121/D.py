from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

A, B = map(int, input().split())
if A == B:
    print(A)
    exit()

if A%2 and B%2:
    diff = (B-A)//2
    if diff%2:
        ans = 1
    else:
        ans = 0
    ans ^= A
elif A%2 and B%2 == 0:
    diff = (B-A-1)//2
    if diff%2:
        ans = 1
    else:
        ans = 0
    ans ^= A
    ans ^= B
elif A%2 == 0 and B%2== 0:
    diff = (B-A)//2
    if diff%2:
        ans = 1
    else:
        ans = 0
    ans ^= B
else:
    diff = (B-A+1)//2
    if diff%2:
        ans = 1
    else:
        ans = 0
print(ans)



