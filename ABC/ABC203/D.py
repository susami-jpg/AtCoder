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
A = [list(map(int, input().split())) for _ in range(N)]

def A_to_bin(A, x):
    new_A = [[0] * (N+1) for _ in range(N+1)]
    for i in range(N):
        for j in range(N):
            if A[i][j] > x:
                new_A[i+1][j+1] = 1
    return new_A

def acc_A(A):
    for i in range(1, N+1):
        for j in range(N+1):
            A[i][j] += A[i-1][j]
    for i in range(N+1):
        for j in range(1, N+1):
            A[i][j] += A[i][j-1]
    return A
            
def is_ok(x):
    new_A = A_to_bin(A, x)
    new_A = acc_A(new_A)
    for i in range(K, N+1):
        for j in range(K, N+1):
            acc_S = new_A[i][j] - new_A[i-K][j] - new_A[i][j-K] + new_A[i-K][j-K]
            if acc_S < (K**2)//2+1:
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

ans = meguru_bisect(-1, INF)
print(ans)
