from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

N = int(input())
player = []
days = set()
for _ in range(N):
    a, b = map(int, input().split())
    days.add(a)
    days.add(a+b)
    player.append((a, a+b))
days = list(days)
days.sort()

def CC(A: list) -> list:
    '座標圧縮'
    B = {j: i for i, j in enumerate(sorted(A))}
    C = {i: j for i, j in enumerate(sorted(A))}
    return B, C

D = len(days)
days, ind = CC(days)
rec = [0] * D
for s, e in player:
    s = days[s]
    e = days[e]
    rec[s] += 1
    rec[e] -= 1
    
rec = list(accumulate(rec))
ans = defaultdict(int)
for i in range(D-1):
    ans[rec[i]] += ind[i+1]-ind[i]

for k in range(1, N+1):
    print(ans[k])


N = int(input())
event = []
for _ in range(N):
    A, B = map(int, input().split())
    event.append((A, 1))
    event.append((A+B, -1))

event.sort()
rec = defaultdict(int)
now = 0
S = 0
for nxt, a in event:
    rec[S] += nxt-now
    S += a
    now = nxt
for i in range(1, N+1):
    print(rec[i])

    

    


