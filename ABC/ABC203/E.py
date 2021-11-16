from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt, factorial
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

N, M = map(int, input().split())
black_porn = defaultdict(set)
x_set = set()
for _ in range(M):
    x, y = map(int, input().split())
    black_porn[x].add(y)
    x_set.add(x)
x_set = sorted(list(x_set))
S = set()
#print(black_porn)
#print(x_set)
S.add(N)
n = len(x_set)
for i in range(n):
    nxtx = x_set[i]
    add_set = set()
    for y in black_porn[nxtx]:
        if y-1 in S:
            add_set.add(y)
        if y+1 in S:
            add_set.add(y)
    for y in black_porn[nxtx]:
        if y in S:
            S.remove(y)
    S |= add_set
    #print(S)
    
print(len(S))
