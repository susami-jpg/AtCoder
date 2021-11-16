from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right
from collections import defaultdict, deque
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
INF = 10**15
MOD = 10**9+7

H, W = map(int, input().split())
setrecursionlimit(10**7)
maze = ["#" + input() + "#" for _ in range(H)]
maze = ["#" * (W+2)] + maze + ["#" * (W+2)]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
ans = -1
def dfs(y, x, sy, sx, seen, d):
    global ans
    if y == sy and x == sx:
        if d >= 3:
            ans = max(ans, d)
        return
    seen[y][x] = 1
    for i in range(4):
        nexty = y + dy[i]
        nextx = x + dx[i]
        if maze[nexty][nextx] == "#":continue
        if seen[nexty][nextx]:continue
        dfs(nexty, nextx, sy, sx, seen, d+1)
    seen[y][x] = 0

for i in range(1, H+1):
    for j in range(1, W+1):
        if maze[i][j] == "#":continue
        for k in range(4):
            nexty = i + dy[k]
            nextx = j + dx[k]
            if maze[nexty][nextx] == ".":
                visited = [[0] * (W+2) for _ in range(H+2)]
                dfs(nexty, nextx, i, j, visited, 1)

print(ans)



