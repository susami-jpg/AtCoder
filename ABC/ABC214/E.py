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

T = int(input())

def is_ok():
    N = int(input())
    balls = [tuple(map(int, input().split())) for _ in range(N)]
    #番兵
    balls.append((INF, INF))
    balls.sort()
    #座標xまでで使えるballの区間の右端をもつheap_queue
    hq = []
    x = 0
    #左端の締め切りが早いものから見ていく
    for l, r in balls:
        #今使えるballを締め切りの近いものから箱に入れていく
        print(l, r)
        print(hq)
        while hq and x < l:
            min_r = hq[0]
            #今見ているxの箱に入れられるballの最小値のballが入れられないならFalse
            if min_r < x:
                return False
            #xにballを入れて次の箱を見る
            heappop(hq)
            x += 1
        #xをlまで移動させる
        x = l
        heappush(hq, r)
    return True

for _ in range(T):
    if is_ok():
        print("Yes")
    else:
        print("No")
        