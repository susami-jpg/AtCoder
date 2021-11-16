from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right
from collections import defaultdict, deque
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import deepcopy
INF = 10**15
MOD = 10**9+7

H, W, K = map(int, input().split())
choco = [[0]*(W+1)] + [[0] + list(map(int, list(input()))) for _ in range(H)]
acc = deepcopy(choco)
for i in range(H+1):
    for j in range(W):
        acc[i][j+1] += acc[i][j]

for j in range(W+1):
    for i in range(H):
        acc[i+1][j] += acc[i][j]

def acc_cnt(y1, x1, y2, x2):
    return acc[y2][x2] - acc[y2][x1-1] - acc[y1-1][x2] + acc[y1-1][x1-1]

def check(prev_cut, now_cut, cut_y):
    x1 = prev_cut
    x2 = now_cut
    for i in range(1, len(cut_y)):
        #前のcut位置+1が今求める範囲
        y1 = cut_y[i-1] + 1
        y2 = cut_y[i]
        if acc_cnt(y1, x1, y2, x2) > K:
            return False
    else:
        return True

ans = INF
for i in range(1 << (H-1)):
    cnt = 0
    cut_y = [0]
    for j in range(H-1):
        if (i>>j)&1:
            cut_y.append(j+1)
            cnt += 1
    cut_y.append(H)

    prev_cut = 1
    for now_cut in range(1, W+1):
        if check(prev_cut, now_cut, cut_y):
            continue
        prev_cut = now_cut
        if not check(prev_cut, prev_cut, cut_y):break
        cnt += 1
    else:
        ans = min(ans, cnt)

print(ans)

    


