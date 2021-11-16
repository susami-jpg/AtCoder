from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt, factorial
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

N, M = map(int, input().split())
edge = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append(b)
    edge[b].append(a)

deq = deque()
deq.append(0)
dist = [INF] * N
dist[0] = 0
vs = []
while deq:
    v = deq.popleft()
    vs.append(v)
    for nextv in edge[v]:
        if dist[nextv] != INF:continue
        dist[nextv] = dist[v] + 1
        deq.append(nextv)

dp = [0] * N
dp[0] = 1
#vsには始点に近い順にvが入っているのでDAGになっている
#DAGなのでdp更新がうまくいく(後ろからの更新は不可)
for v in vs:
    for nextv in edge[v]:
        if dist[nextv] == dist[v] + 1:
            dp[nextv] += dp[v]
            dp[nextv] %= MOD

print(dp[N-1])
