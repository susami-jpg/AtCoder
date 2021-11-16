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

#factorialを使ったnCk
def combinations_count(n, r):
    return factorial(n) // (factorial(n-r) * factorial(r))

#逆元によるnCkの高速計算
def inv(n): # MODを法とした逆元
    MOD = 10**9+7
    return pow(n, MOD-2, MOD)

MOD = 10**9+7
mx = 2*10**5
fact = [1] * (mx+1) # 階乗を格納するリスト
for i in range(mx):
    fact[i+1] = fact[i] * (i+1) % MOD # 階乗を計算

def comb(n, k):
    MOD = 10**9+7
    return (fact[n] * inv(fact[n-k]) * inv(fact[k])) % MOD # comb(n,k) = n!/((n-k)!k!)

#前計算なしver
def combination(n, k):
    nCk = under = top = 1
    mod = 10 ** 9 + 7

    # 分母
    for i in range(2, k + 1):
        under *= i
        under %= mod

    # 分子
    for i in range(k):
        top *= (n - i)
        top %= mod

    nCk = top * pow(under, mod - 2, mod)

    return nCk % mod

N = int(input())
K = int(input())
print(comb(N-1+K, K))
