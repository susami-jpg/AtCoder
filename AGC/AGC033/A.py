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
deq = deque()
dist = [[INF] * W for _ in range(H)]
for i in range(H):
    for j in range(W):
        if maze[i][j] == "#":
            deq.append((i, j))
            dist[i][j] = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def valid(y, x):
    return 0<=y<H and 0<=x<W and maze[y][x] == "."

ans = 0
while deq:
    y, x = deq.popleft()
    for i in range(4):
        nexty, nextx = y+dy[i], x+dx[i]
        if not valid(nexty, nextx):continue
        if dist[nexty][nextx] != INF:continue
        dist[nexty][nextx] = dist[y][x] + 1
        ans = max(dist[nexty][nextx], ans)
        deq.append((nexty, nextx))
print(ans)

        
        

