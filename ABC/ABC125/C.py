from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

N = int(input())
A = list(map(int, input().split()))

setrecursionlimit(10**7)
def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x%y)

left = [0] * N
left[0] = A[0]
right = [0] * N
right[N-1] = A[N-1]
for i in range(1, N):
    left[i] = gcd(A[i], left[i-1])
    right[N-i-1] = gcd(A[N-i-1], right[N-i])
left = [0] + left
right = right + [0]

ans = 1
for i in range(N+1):
    ans = max(ans, gcd(left[i-1], right[i]))

print(ans)

    