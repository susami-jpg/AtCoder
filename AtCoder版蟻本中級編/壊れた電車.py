from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right
from collections import defaultdict, deque
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
INF = 10**15
MOD = 10**9+7

N, M = map(int, input().split())

X = [int(input()) for _ in range(M)]

def is_ok(T):
    #D[i]:= i人目の整備士がT秒で整備できるもっとも右の車両
    D = [0] * M
    for i in range(M):
        if i == 0:
            #X[i]は1-indexedであることに注意
            L = X[i] - 1
        else:
            L = X[i] - D[i-1] - 1
        if L > T:return False
        R = max(T - 2*L, (T-L)//2, 0)
        if i < M-1:
            R = min(R, X[i+1]-X[i]-1)
        D[i] = X[i] + R
    if D[-1] >= N:
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

ans = meguru_bisect(-1, 2*10**9)
print(ans)
