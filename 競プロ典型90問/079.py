from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
INF = 10**15
MOD = 10**9+7

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
B = [list(map(int, input().split())) for _ in range(H)]
ans = 0
for i in range(H-1):
    for j in range(W-1):
        diff = B[i][j] - A[i][j]
        for a in range(2):
            for b in range(2):
                A[i+a][j+b] += diff
        ans += abs(diff)
if A == B:
    print("Yes")
    print(ans)
else:
    print("No")
