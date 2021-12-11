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
MOD = 998244353

N = int(input())
A = list(map(int, input().split()))

def CC(A: list) -> list:
    '座標圧縮'
    #index -> 実際の値のdict
    B = {}
    #実際の値 -> indexのdict
    C = {}
    for i, j in enumerate(sorted(A)):
        B[i] = j
        C[j] = i
    return B, C

ind_to_val, val_to_ind = CC(set(A))
n = len(ind_to_val)
bit = [0] * (n+1)
def get(i):
    s = 0
    while i > 0:
        s += bit[i]
        i -= i & -i
    return s

def add(i, x):
    while i <= n:
        bit[i] += x
        i += i & -i
    return

ans = 0
inv_2 = pow(2, MOD-2, MOD)
for r in range(N):
    v = val_to_ind[A[r]]
    ans += pow(2, r, MOD) * get(v+1)
    ans %= MOD
    add(v+1, pow(inv_2, r+1, MOD))
print(ans)

    
        

