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

def popcount(x):
    '''xの立っているビット数をカウントする関数
    (xは64bit整数)'''

    # 2bitごとの組に分け、立っているビット数を2bitで表現する
    x = x - ((x >> 1) & 0x5555555555555555)

    # 4bit整数に 上位2bit + 下位2bit を計算した値を入れる
    x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)

    x = (x + (x >> 4)) & 0x0f0f0f0f0f0f0f0f # 8bitごと
    x = x + (x >> 8) # 16bitごと
    x = x + (x >> 16) # 32bitごと
    x = x + (x >> 32) # 64bitごと = 全部の合計
    return x & 0x0000007f

N = int(input())
edges = []
for _ in range(N-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges.append((a, b))

dp = dict()
for v in range(N):
    dp[1<<v] = 1
    
def dfs(S):
    if S in dp:
        return dp[S]
    res = 0
    for a, b in edges:
        if ((S>>a)&1 and (S>>b)&1):
            res += dfs(S^(1<<a))
            res %= MOD
            res += dfs(S^(1<<b))
            res %= MOD
    dp[S] = res
    return res

ans = dfs((1<<N)-1)//2
print(ans%MOD)

