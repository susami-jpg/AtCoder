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

A = input()
N = len(A)
cnt = 0
ind = -1
for i in range(N):
    if i > N-i-1:break
    if A[i] != A[N-i-1]:
        cnt += 1
        ind = i

ans = 0
#print(cnt)
for i in range(N):
    if i > N-i-1:break
    if cnt == 0:
        if i == N-i-1:
            break
        else:
            ans += 50
    else:
        if i == N-i-1:
            ans += 25
        else:
            if A[i] == A[N-i-1]:
                ans += 50
            else:
                if cnt == 1:
                    ans += 48
                else:
                    ans += 50
print(ans)
