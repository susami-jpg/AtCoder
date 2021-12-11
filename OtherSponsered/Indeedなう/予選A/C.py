from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt, factorial
from decimal import Decimal
#decimalには文字列で渡す PyPyは遅いのでPython3で提出する
#d1 = Decimal('1.1') d2 = Decimal('2.3') -> d1 + d2などの演算で浮動小数点数での誤差がなくなる(割り算もok)
INF = 10**18
MOD = 10**9+7
setrecursionlimit(10**7)

N = int(input())
mx = 10**6 + 3
scores = [0] * mx
for _ in range(N):
    s = int(input())
    scores[s] += 1

scores = list(accumulate(scores[::-1]))
def OrLessThan(K: int, A: list) -> int:
    '配列Aの中のうち、k以下の個数と終わりの0indexを返すライブラリ'
    '-1の時は解が無い時'
    ans = bisect_right(A, K)
    return ans, (-1 if ans == 0 else ans - 1)

def get_border(k):
    _, points = OrLessThan(k, scores)
    border = mx-points-1
    if scores[points] == scores[-2]:
        return 0
    else:
        return border

Q = int(input())

#ans = []
for _ in range(Q):
    #ans.append(get_border(int(input())))
    print(get_border(int(input())))
#print(*ans)
