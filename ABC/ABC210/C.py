from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt, factorial
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

N, K = map(int, input().split())
C = list(map(int, input().split()))
rec = defaultdict(int)
ans = 0
cnd = 0
for i in range(N):
    if i < K:
        if rec[C[i]] == 0:
            cnd += 1
        rec[C[i]] += 1
    else:
        #先に仲間から外れるやつを引いてあげないとバグる
        #ex
        #N = 6, K = 3
        #[2, 3, 1, 2, 1, 2]
        #i = 3, i-K = 0　のとき、本来の種類数-1になってしまう
        #仲間になるやつをさきに考慮する場合i=3のとき2はすでにあると判定
        #よって種類数は増えない(この時にrecに2を足してればバグらない)
        #仲間から外れるやつを見るときに種類数がひかれてしまう
        rec[C[i-K]] -= 1
        if rec[C[i-K]] == 0:
            cnd -= 1
        if rec[C[i]] == 0:
            cnd += 1
        rec[C[i]] += 1
    ans = max(ans, cnd)
print(ans)

