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
vector_set = set()

def gcd(x, y):
    if x == 0:return y
    else:
        return gcd(y%x, x)

#aが分子でbが分母の有理数を約分して返す
#分母bが0ならa=1、b=0として返す
#a=0の場合は考慮していないので注意
#bは正に変換する
def rational_nun(a, b):
    if b == 0:
        return (1, 0)
    if b < 0:
        a *= -1
        b *= -1
    g = gcd(abs(a), b)
    a //= g
    b //= g
    return (a, b)

#二つの有理数の大小を比較してその大小を返す
#r1、r2は(a, b)の形で渡す(aは分子、bは分母)
#r1 > r2なら1を返す
#r1 == r2なら0を返す
#r1 < r2なら-1を返す
def compare(r1, r2):
    res = r1[0]*r2[1] - r2[0]*r1[1]
    if res > 0:
        return 1
    elif res == 0:
        return 0
    else:
        return -1

for i in range(N-1):
    for j in range(i+1, N):
        dx = plots[i][0] - plots[j][0]
        dy = plots[i][1] - plots[j][1]
        r = rational_nun(dx, dy)
        vector_set.add(r)
print(len(vector_set) * 2)

        