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

N, A, B = map(int, input().split())
P, Q, R, S = map(int, input().split())
ans = [["."] * (S-R+1) for _ in range(Q-P+1)]
l1 = max(1-A, 1-B)
r1 = min(N-A, N-B)
l2 = max(1-A, B-N)
r2 = min(N-A, B-1)

for i in range(P, Q+1):
    for j in range(R, S+1):
        if l1 <= r1 and (A+l1 <= i <= A+r1):
            k = i - A
            if j - B == k and (B+l1 <= j <= B+r1):
                ans[i-P][j-R] = "#"
                #print(i+P+1, j+R+1, 1)
        if l2 <= r2 and (A+l2 <= i <= A+r2):
            k = i - A
            if B - j == k and (B-r2 <= j <= B-l2):
                ans[i-P][j-R] = "#"
                #print(i+P+1, j+R+1, 2)
        

for row in ans:
    print("".join(row))
    
