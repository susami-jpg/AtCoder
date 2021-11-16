from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

N, P, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

#dist(i, j) <= Pとなるような(i, j)の組み合わせがK個未満ならTrue
def is_ok(x):
    dist = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if A[i][j] == -1:
                dist[i][j] = x
            else:
                dist[i][j] = A[i][j]
    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    cnt = 0
    for i in range(N-1):
        for j in range(i+1, N):
            if dist[i][j] <= P:
                cnt += 1
    if cnt < K:
        return True
    else:
        return False

def meguru_bisect(ng, ok):
    '''
    初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
    まずis_okを定義すべし
    ng ok は  とり得る最小の値-1 とり得る最大の値+1
    最大最小が逆の場合はよしなにひっくり返す
    '''
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

R = meguru_bisect(0, INF)

def is_ok(x):
    dist = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if A[i][j] == -1:
                dist[i][j] = x
            else:
                dist[i][j] = A[i][j]
    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    cnt = 0
    for i in range(N-1):
        for j in range(i+1, N):
            if dist[i][j] <= P:
                cnt += 1
    if cnt <= K:
        return True
    else:
        return False
L = meguru_bisect(0, INF)
if R - L <= 0:
    print(0)
elif R == INF:
    print('Infinity')
else:
    print(R-L) 
    