from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

setrecursionlimit(10**7)
maze = [list(input()) for _ in range(10)]
for i in range(10):
    for j in range(10):
        if maze[i][j] == "x":
            maze[i][j] = 0
        else:
            maze[i][j] = 1
            
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def valid(i, j):
    return 0 <= i < 10 and 0 <= j < 10 and maze[i][j]

def dfs(y, x):
    seen[y][x] = 1
    for i in range(4):
        nexty = y + dy[i]
        nextx = x + dx[i]
        if not valid(nexty, nextx):continue
        if seen[nexty][nextx]:continue
        dfs(nexty, nextx)
    return
    
for i in range(10):
    for j in range(10):
        if maze[i][j]:continue
        maze[i][j] = 1
        seen = [[0] * 10 for _ in range(10)]
        dfs(i, j)
        if maze == seen:
            print("YES")
            exit()
        maze[i][j] = 0
print("NO")