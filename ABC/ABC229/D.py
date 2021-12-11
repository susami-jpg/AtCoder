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

S = input()
K = int(input())

N = len(S)
s = []
for i in range(N):
    if S[i] == "X":
        s.append(0)
    else:
        s.append(1)
S = s

#合計がK以下である範囲の最大長を求める
def syakutori3(A, K):
    ans = 0
    A = [0] + A
    n = len(A)
    r = 0
    S = 0
    for l in range(n-1):
        while r+1 < n and S + A[r+1] <= K:
            S += A[r+1]
            r += 1
        ans = max(ans, r-l)
        S -= A[l+1]
    return ans


ans = syakutori3(S, K)
print(ans)

