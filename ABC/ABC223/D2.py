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

N, M = map(int, input().split())
edge = [[] for _ in range(N)]
edge_cnt = [0] * N
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append(b)
    edge_cnt[b] += 1

hq = []
for v in range(N):
    if edge_cnt[v] == 0:
        hq.append(v)

if not hq:
    exit(print(-1))
    
ans = []
while hq:
    v = heappop(hq)
    ans.append(v+1)
    for nextv in edge[v]:
        edge_cnt[nextv] -= 1
        if edge_cnt[nextv] == 0:
            heappush(hq, nextv)

if len(ans) == N:
    print(*ans)
else:
    print(-1)
    
    
