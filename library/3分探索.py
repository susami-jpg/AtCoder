from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt, factorial
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

#目的関数
def f(x):
    return

def ternary_search(low=0, high=INF):
    #while abs(high-low) > 1:
    for _ in range(500):
        c1 = (low*2 + high) / 3
        c2 = (low + high*2) / 3
        
        #もしf(c2)のほうがいい(小さい)なら、ダメなほうlowを更新する
        if f(c1) > f(c2):
            low = c1
        else:
            high = c2
    
    return f(low)

def ternary_search2():
    bottom = 0
    top = INF
    while abs(top-bottom) > 1:
        mid = (top + bottom) / 2
        if f(mid-1) > f(mid):
            bottom = mid
        else:
            top = mid
    return f(bottom)


        