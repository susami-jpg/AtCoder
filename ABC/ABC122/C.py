from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

N, Q = map(int, input().split())
S = ' ' + input()
acc = [0] * (N+1)
for i in range(1, N+1):
    if S[i-1:i+1] == 'AC':
        acc[i] += 1

acc = list(accumulate(acc))

for _ in range(Q):
    l, r = map(int, input().split())
    ans = acc[r]-acc[l-1]
    if S[l-1:l+1] == 'AC':
        ans -= 1
    print(ans)
    

    