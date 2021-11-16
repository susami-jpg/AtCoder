from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

"""
N = int(input())
A = []
for _ in range(N):
    a = list(map(int, input().split()))
    a = list(map(lambda x: x-1, a))[::-1]
    A.append(a)

game = set()
def check(i):
    if len(A[i]) == 0:
        return
    op = A[i][-1]
    if A[op][-1] == i:
        if i > op:
            i, op = op, i
        game.add((i, op))

day = 0
geme_cnt = 0
for i in range(N):
    check(i)
while game:
    day += 1
    prenode_game = game
    game = set()
    for i, j in prenode_game:
        A[i].pop()
        A[j].pop()
        geme_cnt += 1
    for i, j in prenode_game:
        check(i)
        check(j)

if geme_cnt == N*(N-1)//2:
    print(day)
else:
    print(-1)
"""

N = int(input())
A = []
setrecursionlimit(10**7)
for _ in range(N):
    a = list(map(int, input().split()))
    a = list(map(lambda x: x-1, a))
    A.append(a)

node = [[-1] * N for _ in range(N)]
V = 0
for i in range(N-1):
    for j in range(i+1, N):
        node[i][j] = V
        node[j][i] = V
        V += 1

edge = [set() for _ in range(V)]
for i in range(N):
    for j in range(len(A[0])-1):
        f = node[i][A[i][j]]
        t = node[i][A[i][j+1]]
        edge[f].add(t)

dp = [-1] * V
seen = [0] * V
def dfs(v):
    #print(dp)
    #print(seen)
    if seen[v]:
        if dp[v] == -1:
            return -1
        else:
            return dp[v]
    seen[v] = 1
    s = 1
    for nextv in edge[v]:
        res = dfs(nextv)
        if res == -1:return -1
        s = max(s, res + 1)
    dp[v] = s
    return s

ans = 0
for v in range(V):
    res = dfs(v)
    if res == -1:
        exit(print(-1))
    ans = max(ans, res)
print(ans)
