from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
INF = 10**15
MOD = 10**9+7

N = int(input())
A = list(map(int, input().split()))
S = sum(A)
A *= 2
acc = 0
i = 0
deq = []
while i < 2*N:
    acc += A[i]
    deq.append(i)
    if acc == S/10:
        print("Yes")
        break
    while deq and acc > S/10:
        p = deq.pop(0)
        acc -= A[p]
    i += 1
else:
    print("No")
