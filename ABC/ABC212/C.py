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
A = list(map(int, input().split()))
B = list(map(int, input().split()))
B.append(INF)
B.append(-INF)
B.sort()
ans = INF
def OrLessThan(K: int, A: list) -> int:
    '配列Aの中のうち、k以下の個数と終わりの0indexを返すライブラリ'
    '-1の時は解が無い時'
    ans = bisect_right(A, K)
    return ans, (-1 if ans == 0 else ans - 1)

for i in range(N):
    a = A[i]
    _, ind = OrLessThan(a, B)
    b1 = B[ind]
    b2 = B[ind+1]
    ans = min(ans, abs(a-b1), abs(a-b2))
print(ans)

    