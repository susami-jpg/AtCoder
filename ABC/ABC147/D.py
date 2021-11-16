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
A = list(map(int, input().split()))

#keta[i][j]: j=0 or 1でAiをbit変換したときにi桁目が0であるAがいくつあるか、i桁目が1である項がいくつあるか記録
keta = [[0] * 2 for _ in range(61)]
for k in range(N):
    for i in range(61):
        keta[i][(A[k]>>i)&1] += 1

ans = 0

#各桁について独立に考えた時にxor計算で1となるのは、一方が1で他方が0のとき
for i in range(61):
    ans += pow(2, i) * keta[i][0] * keta[i][1]
    ans %= MOD
print(ans)
