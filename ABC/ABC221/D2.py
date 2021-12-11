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
day_set = set()
player = []
for _ in range(N):
    a, b = map(int, input().split())
    day_set.add(a)
    day_set.add(a+b)
    player.append((a, a+b))

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

n = len(day_set)
ind_to_day, day_to_ind = CC(list(day_set))
acc_login = [0] * n
#print(day_to_ind)
for a, b in player:
    a = day_to_ind[a]
    b = day_to_ind[b]
    acc_login[a] += 1
    acc_login[b] -= 1
#print(acc_login)
acc_login = list(accumulate(acc_login))
#print(acc_login)
D = [0] * (N+1)
for i in range(n-1):
    prev = ind_to_day[i]
    nxt = ind_to_day[i+1]
    D[acc_login[i]] += nxt-prev
print(*D[1:])


N = int(input())
player = []
for _ in range(N):
    a, b = map(int, input().split())
    player.append((a, 1))
    player.append((a+b, -1))

player.sort()
s = 0
prev = 0
D = [0] * (N+1)
for day, val in player:
    D[s] += (day-prev)
    prev = day
    s += val
print(*D[1:])