from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt, factorial
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

N = int(input())
S = list(map(int, input().split()))
T = int(input())
prev = 0
S.sort()

now = T
seen = 0
def LessThan(K: int, A: list) -> int:
    '配列Aの中のうち、k未満の個数と終わりの0indexを返すライブラリ'
    '-1の時は解が無い時'
    ans = bisect_left(A, K)
    return ans, (-1 if ans == 0 else ans - 1)

ans = 0
while seen < N:
    k, ind = LessThan(now, S)
    #print(k, ind)
    #print(seen)
    if k - seen:
        seen += k-seen
        ans += 1
    now += T
print(ans)

    