from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
INF = 10**15
MOD = 10**9+7

H, W = map(int, input().split())
maze = [["#"] + list(input()) + ["#"] for _ in range(H)]
maze = [["#"] * (W+2)] + maze + [["#"] * (W+2)]

def bfs(sy, sx):
    deq = deque()
    deq.append((sy, sx, 0))
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    seen = [[-1] * (W+2) for _ in range(H+2)]
    while deq:
        y, x, d = deq.popleft()
        if seen[y][x] != -1:
            continue
        seen[y][x] = d
        for i in range(4):
            nexty = y + dy[i]
            nextx = x + dx[i]
            if maze[nexty][nextx] == "." and seen[nexty][nextx] == -1:
                deq.append((nexty, nextx, d+1))
    dist_max = 0
    for i in range(1, H+1):
        for j in range(1, W+1):
            dist_max = max(dist_max, seen[i][j])
    return dist_max


ans = 0
for sy in range(1, H+1):
    for sx in range(1, W+1):
        if maze[sy][sx] == "#":continue
        ans = max(ans, bfs(sy, sx))

print(ans)


