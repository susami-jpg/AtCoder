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

N = 9
M = int(input())
edge = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    edge[u].append(v)
    edge[v].append(u)
    
goal = [i for i in range(1, 9)] + [0]
s = list(map(int, input().split()))
start = [0] * 9
for i in range(8):
    start[s[i]-1] = i+1

def encode(v):
    v = list(map(str, v))
    return int("".join(v))

start = tuple(start)
dist = dict()
deq = deque()
deq.append(start)
dist[encode(start)] = 0
while deq:
    v = list(deq.popleft())
    pd = dist[encode(v)]
    if v == goal:
        exit(print(pd))
    vacant = v.index(0)
    for nextv in edge[vacant]:
        v[vacant], v[nextv] = v[nextv], v[vacant]
        if encode(v) not in dist:
            deq.append(tuple(v))
            dist[encode(v)] = pd + 1
        v[vacant], v[nextv] = v[nextv], v[vacant]
print(-1)



