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
X = int(input())
acc_A = [0] * N
acc_A[0] = A[0]
for i in range(1, N):
    acc_A[i] = acc_A[i-1] + A[i]

def More(K: int, A: list) -> int:
    '配列Aの中のうち、kより大きいものの個数と始まりの0indexを返すライブラリ'
    '-1の時は解が無い時'
    ans = bisect_right(A, K)
    l = len(A)
    return l - ans, (ans if ans <= l - 1 else -1)

max_A = acc_A[-1]
if max_A > X:
    _, ans = More(X, acc_A)
    print(ans+1)
else:
    ans = 0
    ans += (X//max_A)*N
    X %= max_A
    _, ind = More(X, acc_A)
    ans += ind
    print(ans+1)
    

