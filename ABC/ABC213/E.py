from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt, factorial
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

H, W = map(int, input().split())
S = [input() for _ in range(H)]
def valid(y, x):
    return 0<=y<=H-1 and 0<=x<=W-1

dist = [[INF] * W for _ in range(H)]
dist[0][0] = 0
deq = deque()
deq.append((0, 0))
ban = [(-2, -2), (2, -2), (-2, 2), (2, 2), (0, 0)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
while deq:
    y, x = deq.popleft()
    for i in range(4):
        nexty = y+dy[i]
        nextx = x+dx[i]
        if not valid(nexty, nextx):continue
        if S[nexty][nextx] == "#":continue
        if dist[nexty][nextx] > dist[y][x]:
            dist[nexty][nextx] = dist[y][x]
            deq.appendleft((nexty, nextx))
    for i in range(-2, 3):
        for j in range(-2, 3):
            if (i, j) in ban:continue
            nexty = y+i
            nextx = x+j
            if not valid(nexty, nextx):continue
            if dist[nexty][nextx] > dist[y][x] + 1:
                dist[nexty][nextx] = dist[y][x] + 1
                deq.append((nexty, nextx))
print(dist[H-1][W-1])