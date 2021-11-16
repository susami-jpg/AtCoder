from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt, gcd
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7


#SPFによる前処理とクエリの高速素数判定

#SmallestPrimeFactor
#自分の素因数の中で最小の素因数を記録
#前処理O(NloglogN)
#nは調べたい範囲の最大値
def SPF(n):
    spf = [i for i in range(n + 1)]
    check = [False] * (n + 1)
    spf[0] = 0
    spf[1] = 1
    check[0] = check[1] = True
    for i in range(2, int(n**0.5) + 1):
        if check[i]: continue
        for j in range(i, n + 1, i):
            if check[j]:continue
            spf[j] = i
            check[j] = True
    return spf


"""
primefactは素因数分解した結果を返す
ただしsetではない
ex: 9 -> 3, 3を返す
"""
#上のSPFによる前処理を終えた前提(関数内のspfは上の関数を使用した返り値のリストを参照している)
#クエリごとにO(logN)で素因数分解した結果を返す
#素因数分解なのでn=0,1はエラーを吐くので注意
def primefact(n, spf):
    fact = []
    while n != 1:
        fact.append(spf[n])
        n //= spf[n]
    return fact

spf = SPF(10**6+1)
N = int(input())
A = list(map(int, input().split()))
rec = defaultdict(int)
for a in A:
    for key, val in Counter(primefact(a, spf)).items():
        if rec[key] < val:
            rec[key] = val
lcm = 1
for key, val in rec.items():
    lcm *= pow(key, val, MOD)
    
ans = 0
for a in A:
    ans += lcm*pow(a, MOD-2, MOD)
    ans %= MOD
print(ans)
