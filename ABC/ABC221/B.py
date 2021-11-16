from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

S = input()
T = input()
N = len(S)
if S == T:
    print('Yes')
    exit()
for i in range(N-1):
    s = S[:i] + S[i+1] + S[i] + S[i+2:]
    if s == T:
        print('Yes')
        break
else:
    print('No')
    
        