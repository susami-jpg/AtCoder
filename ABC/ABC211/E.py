from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt, factorial
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

setrecursionlimit(10**7)
N = int(input())
K = int(input())
S = [input() for _ in range(N)]
def valid(y, x):
    return 0<=y<=N-1 and 0<=x<=N-1

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
seen = set()
ans = 0

def map_to_bin(A):
    res = 0
    for i in range(N):
        for j in range(N):
            if A[i][j] == 1:
                ns = i*N+j
                res |= (1<<ns)
    return res

def bin_to_map(res):
    A = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            ns = i*N+j
            if (res>>ns)&1:
                A[i][j] = 1
    return A

def dfs(c, painted):
    if painted in seen:return
    seen.add(painted)
    global ans
    if c == K:
        ans += 1
        return
    red_set = set()
    for i in range(N):
        for j in range(N):
            ns = i*N+j
            if (painted>>ns)&1:
                red_set.add(ns)
    for ns in red_set:
        y = ns//N
        x = ns%N
        for d in range(4):
            nexty = y + dy[d]
            nextx = x + dx[d]
            if not valid(nexty, nextx):continue
            if S[nexty][nextx] == "#":continue
            nexts = nexty*N + nextx
            if (painted>>nexts)&1:continue
            dfs(c+1, painted|(1<<nexts))
    return

for i in range(N):
    for j in range(N):
        if S[i][j] == ".":
            dfs(1, 1<<(i*N+j))
print(ans)



                
                