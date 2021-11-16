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

par = [-1] * 3*10**5
rank = [0] * 3*10**5

def find(x):
    if par[x] < 0:return x
    else:
        par[x] = find(par[x])
        return par[x]

def unite(x, y):
    x = find(x)
    y = find(y)
    if x==y:return
    if rank[x] < rank[y]:
        x, y = y, x
    elif rank[x] == rank[y]:
        rank[x] += 1 
    par[x] += par[y]
    par[y] = x

def size(x):
    return -par[find(x)]


L, Q = map(int, input().split())
ends = [L]
query = [tuple(map(int, input().split())) for _ in range(Q)]
for c, x in query:
    if c == 1:
        ends.append(x)
        
ends.sort()
last = 0
for i in range(len(ends)):
    par[i] = -(ends[i]-last)
    last = ends[i]
#print(ends)
ans = []

for c, x in query[::-1]:
    if c == 1:
        ind = bisect_left(ends, x)
        unite(ind, ind+1)
    else:
        ind = bisect_left(ends, x)
        ans.append(size(ind))

print(*ans[::-1])

