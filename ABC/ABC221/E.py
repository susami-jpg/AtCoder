from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 998244353

N = int(input())
A = list(map(int, input().split()))
def CC(A: list) -> list:
    '座標圧縮'
    B = {j: i for i, j in enumerate(sorted(set(A)))}
    return B
cc = CC(A)
n = len(cc)
BIT = [0] * (n+10)
def add(i, a):
    i += 1
    while i <= n:
        BIT[i] += a
        i += i & -i

def get(i):
    i += 1
    S = 0
    while i:
        S += BIT[i]
        i -= i & -i
    return S

ans = 0
for i in range(N):
    ans += pow(2, max(0, i-1), MOD) * get(cc[A[i]])
    add(cc[A[i]], pow(pow(2, i, MOD), MOD-2, MOD))
    ans %= MOD
print(ans)


        

    
    
        
