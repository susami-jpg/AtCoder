from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

N = int(input())
member = [tuple(map(int, input().split())) for _ in range(N)]

def is_ok(x):
    bin_set = set()
    for p in member:
        c = 0
        for i in range(5):
            if p[i] >= x:
                c |= (1<<i)
        bin_set.add(c)
    
    ok = (1<<5)-1
    for a in bin_set:
        for b in bin_set:
            for c in bin_set:
                if a|b|c == ok:
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

ans = meguru_bisect(10**10, 0)
print(ans)
