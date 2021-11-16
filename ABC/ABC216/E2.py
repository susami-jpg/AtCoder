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

N, K = map(int, input().split())
A = list(map(int, input().split()))
def is_ok(x):
    # 楽しさの最低値をxとしたときにK回以上アトラクションにのれるか?
    cnt = 0
    for i in range(N):
        cnt += max(0, A[i]-x+1)
    if cnt >= K:
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

#初項a、末項l、項数n
def S1(a, l, n):
    return n*(a+l)//2

#初項a、公差d、項数n
def S2(a, d, n):
    return n*(2*a + (n-1)*d)//2

min_x = meguru_bisect(INF, 0)
ans = 0
cnt = 0
for i in range(N):
    ans += S2(min_x, 1, max(0, A[i]-min_x+1))
    cnt += max(0, A[i]-min_x+1)
ans -= (cnt-K)*min_x
print(ans)
