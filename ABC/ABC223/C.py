from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt, factorial
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

N = int(input())
A = []
B = []

for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
#A.append(0)
#B.append(1)
if N == 1:
    print(A[0]/2)
    exit()
A_left = A[:]
for i in range(N-1):
    A_left[i+1] += A_left[i]

def OrLessThan(K: int, A: list) -> int:
    '配列Aの中のうち、k以下の個数と終わりの0indexを返すライブラリ'
    '-1の時は解が無い時'
    ans = bisect_right(A, K)
    return ans, (-1 if ans == 0 else ans - 1)

def is_ok(x):
    _, ind = OrLessThan(x, A_left)
    mid = ind+1
    left_S = 0
    for i in range(ind+1):
        left_S += A[i] / B[i]
    left_S += (x-A_left[ind]) / B[mid]
    right_S = 0
    for i in range(mid+1, N):
        right_S += A[i] / B[i]
    right_S += (A_left[mid]-x) / B[mid]
    if left_S <= right_S:
        return True
    else:
        return False

ok = 0
ng = A_left[-1]+1

for _ in range(100):
    mid = (ok + ng) / 2
    if is_ok(mid):
        ok = mid
    else:
        ng = mid
print(ok)
