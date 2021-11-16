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

N, M = map(int, input().split())
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

#試し割法の素因数分解(1は空のリストを返すので注意)
#O(sqrt(N))
def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

prime_factor = prime_factorize(abs(N))
ans = 1
for key, val in Counter(prime_factor).items():
    ans *= comb(val+M-1, val)
    ans %= MOD

if N > 0:
    prod = 0
    for i in range(0, M+1, 2):
        if i > M:break
        prod += comb(M, i)
        prod %= MOD
else:
    prod = 0
    for i in range(1, M+1, 2):
        if i > M:break
        prod += comb(M, i)
        prod %= MOD

ans *= prod
ans %= MOD
print(ans)
