from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
INF = 10**15
MOD = 10**9+7

H = int(input())
cnt = 0
while H > 0:
    H //= 2
    cnt += 1

#1+2+3+...+nの和
def sigma1(n):
    return n*(n+1)//2

#1**2 + 2**2 + 3**2 +...+ n**2の和
def sigma2(n):
    return n*(n+1)*(2*n+1)//6

#1**3 + 2**3 + 3**3 +...+ n**3の和
def sigma3(n):
    return pow(n*(n+1)//2, 2)

#初項a、公比r、項数nの等比数列の和
def ar(a, r, n):
    return a*(pow(r, n)-1)/(r-1)

ans = ar(1, 2, cnt)
print(int(ans))
