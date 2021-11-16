from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
INF = 10**15
MOD = 10**9+7

input = stdin.readline
N = int(input())
A = [int(input()) for _ in range(N)]
"""
A *= 2
A = list(accumulate(A))

def OrMore(K: int, A: list) -> int:
    '配列Aの中のうち、k以上の個数と始まりの0indexを返すライブラリ'
    '-1の時は解が無い時'
    ans = bisect_left(A, K)
    l = len(A)
    return l - ans, (ans if ans <= l - 1 else -1)

def is_ok(x):
    for i in range(N):
        a = A[i:i+N]
        if i == 0:
            acc = 0
        else:
            acc = A[i-1]
        for _ in range(2):
            _, ind = OrMore(acc+x, a)
            if ind == -1:break
            acc = a[ind]
        last_piece = a[-1] - acc
        if last_piece >= x:
            return True
    else:
        return False
"""

A *= 2
acc_A = list(accumulate(A))

def is_ok(x):
    #nxt[i]:= [i, j)の区間和がx以上になるような最小のj(i < j)
    nxt = [INF] * (2*N)
    acc = 0
    i = 0
    deq = []
    while i < 2*N:
        deq.append(i)
        acc += A[i]
        while deq and acc >= x:
            p = deq.pop(0)
            nxt[p] = i+1
            acc -= A[p]
        i += 1

    for i in range(N):
        s1 = i
        last = i+N-1
        s2 = nxt[s1]
        if s2 > last:continue
        s3 = nxt[s2]
        if s3 > last:continue
        last_piece = acc_A[last] - acc_A[s3-1]
        if last_piece >= x:
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

ans = meguru_bisect(sum(A), 0)
print(ans)
