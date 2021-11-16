from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

N = int(input())
L = list(map(int, input().split()))
L.sort()

def LessThan(K: int, A: list) -> int:
    '配列Aの中のうち、k未満の個数と終わりの0indexを返すライブラリ'
    '-1の時は解が無い時'
    ans = bisect_left(A, K)
    return ans, (-1 if ans == 0 else ans - 1)

def More(K: int, A: list) -> int:
    '配列Aの中のうち、kより大きいものの個数と始まりの0indexを返すライブラリ'
    '-1の時は解が無い時'
    ans = bisect_right(A, K)
    return N - ans, (ans if ans <= N - 1 else -1)

ans = 0
for i in range(N-1):
    for j in range(i+1, N):
        a, b = L[i], L[j]
        r, _ = LessThan(a+b, L)
        ans += max(0, r - (j+1))
print(ans)
        

        