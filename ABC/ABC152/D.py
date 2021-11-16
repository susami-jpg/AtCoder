from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
INF = 10**15
MOD = 10**9+7

N = int(input())
ans = 0
sN = str(N)
L = len(sN)
for A in range(1, N+1):
    sA = str(A)
    a = sA[0]
    b = sA[-1]
    if b == "0":continue
    #1桁の場合
    if a == b:
        ans += 1
    #二桁の場合の数
    if int(b+a) <= N:
        ans += 1
    x = 1
    while x+2 < L:
        ans += pow(10, x)
        x += 1
    if L >= 3:
        if int(b) > int(sN[0]):continue
        cnd = int(sN[1:-1])
        if int(b) == int(sN[0]):
            if int(a) > int(sN[-1]):
                ans += cnd
            else:
                ans += cnd+1
        else:
            ans += pow(10, x)
print(ans)

        
