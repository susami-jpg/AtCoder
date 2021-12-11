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

#再帰構造を意識する
#N%2==1なら今見ている桁のbitは立っていなければいけない
#このとき、今見ている桁を除いた-2進数の数をN'とすると
#今見ている桁が偶数ならN' = N - 1(今見ている桁によって+1されているので)
#今見ている桁が奇数ならN' = N + 1(今見ている桁によって-1されているので)
#こうして計算されたN'を2で割った値について同じ操作を繰り返す(つぎの桁のbitを考えるにはN'を2で割ってbitを全体として右にずらす必要がある)

#これをNを-2で割ることにすると今見ている桁の偶奇を考えずbitが立っていたらNに-1をしてやるだけでよくなる

N = int(input())
if N == 0:
    exit(print(0))
ans = ""
keta = 0
while N != 0:
    if N%2:
        if keta%2:
            N += 1
        else:
            N -= 1
        ans = "1" + ans
    else:
        ans = "0" + ans
    N //= 2
    keta += 1
print(ans)


N = int(input())
if N == 0:
    exit(print(0))
ans = ""
while N != 0:
    if N%2:
        ans = "1" + ans
        N -= 1
    else:
        ans = "0" + ans
    N //= -2
print(ans)
