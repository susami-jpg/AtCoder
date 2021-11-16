from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt, factorial
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

H, W, N = map(int, input().split())
query = []
for i in range(N):
    r, c, a = map(int, input().split())
    r -= 1
    c -= 1
    query.append((a, i, r, c))

query.sort(reverse=True)
#各行のdpの最大値
#dp[i] = i行目のdpの値の最大値を返す
r_max = dict()
#各列のdpの最大値
#dp[i] = i列目のdpの値の最大値を返す
c_max = dict()
r_count = defaultdict(int)
c_count = defaultdict(int)
field = dict()
ans = [-1] * N
for a, i, r, c in query:
    if r_count[r] == 0:
        r_cnd = -1
    else:
        r_cnd, nxt_a = r_max[r][-1]
        #先に更新された行の最高値のaの値が今見ているaの値と同じならそこには移動できないので0
        if a == nxt_a:
            if r_count[r] == 1:
                r_cnd = -1
            else:
                r_cnd, nxt_a = r_max[r][-2]
    if c_count[c] == 0:
        c_cnd = -1
    else:
        c_cnd, nxt_a = c_max[c][-1]
        #先に更新された行の最高値のaの値が今見ているaの値と同じならそこには移動できないので0
        if a == nxt_a:
            if c_count[c] == 1:
                c_cnd = -1
            else:
                c_cnd, nxt_a = c_max[c][-2]
    #print(a, i, r_cnd, c_cnd)
    
    ans[i] = max(r_cnd + 1, c_cnd + 1)
    #行、列の最高値の更新
    if r_count[r] == 0:
        r_max[r] = [(ans[i], a)]
        r_count[r] += 1
    else:
        r_cnd, nxt_a = r_max[r][-1]
        if r_cnd < ans[i]:
            if a == nxt_a:
                r_max[r][-1] = (ans[i], a)
            else:
                r_max[r].append((ans[i], a))
                r_count[r] += 1
    if c_count[c] == 0:
        c_max[c] = [(ans[i], a)]
        c_count[c] += 1
    else:
        c_cnd, nxt_a = c_max[c][-1]
        if c_cnd < ans[i]:
            if a == nxt_a:
                c_max[c][-1] = (ans[i], a)
            else:
                c_max[c].append((ans[i], a))
                c_count[c] += 1
    

for i in range(N):
    print(ans[i])
                