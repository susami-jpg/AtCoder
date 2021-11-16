from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

H, W = map(int, input().split())
maze = [input() for _ in range(H)]
for i in range(H):
    for j in range(W):
        if maze[i][j] == "s":
            sy, sx = i, j
        elif maze[i][j] == "g":
            gy, gx = i, j

def valid(y, x):
    return 0<=y<H and 0<=x<W

def bfs01(sy, sx, gy, gx):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    dist = [[INF] * W for _ in range(H)]
    dist[sy][sx] = 0
    deq = deque()
    deq.append((sy, sx))
    while deq:
        y, x = deq.popleft()
        if y == gy and x == gx:
            break
        for i in range(4):
            nexty = y+dy[i]
            nextx = x+dx[i]
            if not valid(nexty, nextx):continue
            if dist[nexty][nextx] != INF:continue
            if maze[nexty][nextx] != "#":
                dist[nexty][nextx] = dist[y][x]
                deq.appendleft((nexty, nextx))
            else:
                dist[nexty][nextx] = dist[y][x] + 1
                deq.append((nexty, nextx))
    return dist[gy][gx] <= 2

if bfs01(sy, sx, gy, gx):
    print('YES')
else:
    print('NO')
    
                
    