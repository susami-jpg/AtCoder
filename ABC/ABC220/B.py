from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7


########関数部分##############
def Base_n_to_10(X,n):
    out = 0
    for i in range(1,len(str(X))+1):
        out += int(X[-i])*(n**(i-1))
    return out#int out
############################
"""
Xはstr
nはint
戻り値はint

print(Base_n_to_10('253',4))#"55"と表示される．
"""
K = int(input())
A, B = input().split()
ans = Base_n_to_10(A, K) * Base_n_to_10(B, K)
print(ans)
