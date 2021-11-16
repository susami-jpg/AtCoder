from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

X, Y = map(int, input().split())
if (2*X-Y)%3:
    print(0)
    exit()
elif (2*Y-X)%3:
    print(0)
    exit()
    
a = (2*X-Y)//3
b = (2*Y-X)//3

if a < 0 or b < 0:
    print(0)
    exit()
#前計算なしver
def combination(n, k):
    nCk = under = top = 1
    mod = 10 ** 9 + 7

    # 分母
    for i in range(2, k + 1):
        under *= i
        under %= mod

    # 分子
    for i in range(k):
        top *= (n - i)
        top %= mod

    nCk = top * pow(under, mod - 2, mod)

    return nCk % mod

print(combination(a+b, a))
