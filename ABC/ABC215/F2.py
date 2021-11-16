from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt, factorial
from decimal import Decimal
#decimalには文字列で渡す PyPyは遅いのでPython3で提出する
#d1 = Decimal('1.1') d2 = Decimal('2.3') -> d1 + d2などの演算で浮動小数点数での誤差がなくなる(割り算もok)
INF = 10**15
MOD = 10**9+7

N = int(input())
plots = [tuple(map(int, input().split())) for _ in range(N)]
plots.sort()

def is_ok(d):
    prev = 0
    min_y = max_y = None
    for x, y in plots:
        while prev < N and plots[prev][0] <= x-d:
            if min_y == None:
                min_y = max_y = plots[prev][1]
            else:
                min_y = min(min_y, plots[prev][1])
                max_y = max(max_y, plots[prev][1])
            prev += 1
        if min_y != None:
            cnd = max(abs(min_y-y), abs(max_y-y))
            if cnd >= d:
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

ans = meguru_bisect(INF, 0)
print(ans)
