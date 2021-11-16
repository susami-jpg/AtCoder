from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7


#ここからlcm_2まででリスト内の複数の数字の最小公倍数を返す関数
from math import gcd

# 2数を受け取って最小公倍数を返す関数
def lcm(a, b):
    y = a*b // gcd(a, b)
    return int(y)

A, B, C, D = map(int, input().split())
LCM = lcm(C, D)
n1 = B - (B//C + B//D - B//LCM)
A -= 1
n2 = A - (A//C + A//D - A//LCM)
print(n1-n2)
