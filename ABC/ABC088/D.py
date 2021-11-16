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
def valid(y, x):
    return 0<=y<H and 0<=x<W and maze[y][x] == "."

def bfs(sy, sx, gy, gx):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    deq = deque()
    deq.append((sy, sx))
    dist = [[INF] * W for _ in range(H)]
    dist[sy][sx] = 0
    while deq:
        y, x = deq.popleft()
        if y == gy and x == gx:break
        for i in range(4):
            nexty = y+dy[i]
            nextx = x+dx[i]
            if not valid(nexty, nextx):continue
            if dist[nexty][nextx] != INF:continue
            dist[nexty][nextx] = dist[y][x] + 1
            deq.append((nexty, nextx))
    return dist[gy][gx]

black_cnt = 0
L = bfs(0, 0, H-1, W-1)
if L == INF:
    print(-1)
    exit()
for i in range(H):
    for j in range(W):
        if maze[i][j] == "#":
            black_cnt += 1
ans = H*W - black_cnt - (L+1)
print(ans)

