from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt, factorial
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

N, Q = map(int, input().split())
A = list(map(int, input().split()))
def OrLessThan(K: int, A: list) -> int:
    '配列Aの中のうち、k以下の個数と終わりの0indexを返すライブラリ'
    '-1の時は解が無い時'
    ans = bisect_right(A, K)
    return ans, (-1 if ans == 0 else ans - 1)
"""
for _ in range(Q):
    K = int(input())
    diff = 0
    prev_diff = 0
    while 1:
        k, ind = OrLessThan(K, A)
        if k == prev_diff:
            print(K)
            break
        K += k - prev_diff
        prev_diff = k
"""

def LessThan(K: int, A: list) -> int:
    '配列Aの中のうち、k未満の個数と終わりの0indexを返すライブラリ'
    '-1の時は解が無い時'
    ans = bisect_left(A, K)
    return ans, (-1 if ans == 0 else ans - 1)

A = [0] + A
C = [0] * (N+1)
for i in range(1, N+1):
    C[i] += C[i-1] + (A[i]-A[i-1]-1)

for _ in range(Q):
    K = int(input())
    _, ind = LessThan(K, C)
    print(A[ind] + K - C[ind])
    
    