from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

N, M, Q = map(int, input().split())
bag = []
for _ in range(N):
    w, v = map(int, input().split())
    bag.append((v, w))

def OrMore(K: int, A: list) -> int:
    '配列Aの中のうち、k以上の個数と始まりの0indexを返すライブラリ'
    '-1の時は解が無い時'
    ans = bisect_left(A, K)
    l = len(A)
    return l - ans, (ans if ans <= l - 1 else -1)

bag.sort(reverse=True)
box = list(map(int, input().split()))
for _ in range(Q):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    rest = box[:l] + box[r+1:]
    rest.sort()
    ans = 0
    for v, w in bag:
        _, ind = OrMore(w, rest)
        if ind == -1:continue
        ans += v
        rest.pop(ind)
    print(ans)
