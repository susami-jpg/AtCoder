from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
INF = 10**15
MOD = 10**9+7

L, R = map(int, input().split())

ans = 0
l_keta = len(str(L))
r_leta = len(str(R))

i = l_keta
now = L

#初項a、末項l、項数n
def S1(a, l, n):
    return n*(a+l)//2

#初項a、公差d、項数n
def S2(a, d, n):
    return n*(2*a + (n-1)*d)//2

while 1:
    if pow(10, i) > R:
        ans += i * S1(now, R, R-now+1)
        break
    ans += i * S1(now, pow(10, i)-1, pow(10, i)-now)
    now = pow(10, i)
    i += 1
    ans %= MOD
print(ans%MOD)

