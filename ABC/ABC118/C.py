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

# Euclidean Algorithm
def gcd(m, n):
    r = m % n
    return gcd(n, r) if r else n

def gcd_t(A):
    res = A[0]
    for i in range(1, len(A)):
        res = gcd(res, A[i])
    return res

print(gcd_t(A))
