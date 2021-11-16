from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

N, K = map(int, input().split())
V = list(map(int, input().split()))
rec = defaultdict(list)
for l in range(N):
    for r in range(l, N+1):
        rec[(l, r)] = sorted(V[:l] + V[r:])

left = [0] + V
right = V + [0]
for i in range(N):
    left[i+1] += left[i]
    right[N-1-i] += right[N-i]
    

def LessThan(K: int, A: list) -> int:
    '配列Aの中のうち、k未満の個数と終わりの0indexを返すライブラリ'
    '-1の時は解が無い時'
    ans = bisect_left(A, K)
    return ans, (-1 if ans == 0 else ans - 1)

ans = 0
for l in range(N):
    for r in range(l, N+1):
        if l + (N-r) > K:continue
        k = K-(l + (N-r))
        cnt, ind = LessThan(0, rec[(l, r)])
        if cnt > k:
            ans = max(ans, left[l] + right[r] - sum(rec[(l, r)][:k]))
        else:
            ans = max(ans, left[l] + right[r] - sum(rec[(l, r)][:ind+1]))
print(ans)

            