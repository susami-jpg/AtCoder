from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

setrecursionlimit(10**8)
N = int(input())
edge = [[] for _ in range(N)]
A = [[0] * N for _ in range(N)]
for _ in range(N-1):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append((b, c))
    edge[b].append((a, c))
    A[a][b] = c
    A[b][a] = c


D = list(map(int, input().split()))
dp1 = [-1] * N
end = [0] * N
def dfs1(v, par=-1):
    if dp1[v] != -1:
        return dp1[v]
    max_E = D[v]
    cnt = 0
    for nextv, c in edge[v]:
        if par == nextv:continue
        dfs1(nextv, v)
        max_E = max(max_E, dp1[nextv] + c)
        cnt += 1
    dp1[v] = max_E
    if cnt == 0:
        end[v] = 1
    return dp1[v]
dfs1(0)

dp2 = [-1] * N
dp2[0] = D[0]
def dfs2(v, par=-1):
    children = []
    for nextv, c in edge[v]:
        if nextv == par:continue
        children.append(nextv)
    #print(children)
    n = len(children)
    left = [0] * (n+1)
    right = [0] * (n+1)
    for i in range(n):
        left[i+1] = max(dp1[children[i]] + A[v][children[i]], left[i])
        right[n-i-1] = max(dp1[children[n-i-1]] + A[v][children[n-i-1]], right[n-i])
    
    for i, child in enumerate(children):
        dp2[child] = max(dp2[v], left[i], right[i+1]) + A[v][child]
        dfs2(child, v)
    return

dfs2(0)
#print(dp2)

print(dp1[0])
for v in range(1, N):
    if end[v]:
        print(dp2[v])
    else:
        ans = max(dp1[v], dp2[v])
        print(ans)
    
