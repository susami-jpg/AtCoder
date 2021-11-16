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

A = [[0] + list(map(int, input().split())) + [0] for _ in range(4)]
A = [[0] * 6] + A + [[0] * 6]
castle = set()
for i in range(1, 5):
    for j in range(1, 5):
        if A[i][j]:
            castle.add((i-1)*4+j-1)
            
def valid(y, x):
    return 0<=y<6 and 0<=x<6

def bin_to_map(i):
    new_map = [[0] * 6 for _ in range(6)]
    for j in range(16):
        if (i>>j)&1:
            y = j//4
            x = j%4
            new_map[y+1][x+1] = 1
    return new_map

def cas_check(i):
    for j in castle:
        if (i>>j)&1 == 0:
            return False
    else:
        return True

def bfs_check(town, sy, sx):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    seen = [[0] * 6 for _ in range(6)]
    deq = deque()
    deq.append((sy, sx))
    while deq:
        y, x = deq.popleft()
        seen[y][x] = 1
        for i in range(4):
            nexty = y+dy[i]
            nextx = x+dx[i]
            if not valid(nexty, nextx):continue
            if seen[nexty][nextx] or town[nexty][nextx] == 0:continue
            deq.append((nexty, nextx))
    return town == seen

def surround_check(town):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    seen = [[1] * 6 for _ in range(6)]
    deq = deque()
    deq.append((0, 0))
    while deq:
        y, x = deq.popleft()
        seen[y][x] = 0
        for i in range(4):
            nexty = y+dy[i]
            nextx = x+dx[i]
            if not valid(nexty, nextx):continue
            if seen[nexty][nextx] == 0 or town[nexty][nextx]:continue
            deq.append((nexty, nextx))
    return town == seen

ans = 0
for i in range(1<<16):
    if not cas_check(i):continue
    new_map = bin_to_map(i)
    for y in range(1, 5):
        for x in range(1, 5):
            if new_map[y][x]:
                sy = y
                sx = x
                break
        else:
            continue
        break
    if not bfs_check(new_map, sy, sx):continue
    if not surround_check(new_map):continue
    ans += 1
        
print(ans)
