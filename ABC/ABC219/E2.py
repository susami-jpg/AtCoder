from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt, factorial
from decimal import Decimal
#decimalには文字列で渡す PyPyは遅いのでPython3で提出する
#d1 = Decimal('1.1') d2 = Decimal('2.3') -> d1 + d2などの演算で浮動小数点数での誤差がなくなる(割り算もok)
INF = 10**15
MOD = 10**9+7

A = [list(map(int, input().split())) for _ in range(4)]
town_set = set()
for i in range(4):
    for j in range(4):
        if A[i][j]:
            town_set.add((i, j))

def create_field(bit):
    field = [[0] * 4 for _ in range(4)]
    cnt = 0
    for i in range(4):
        for j in range(4):
            if (bit>>(i*4+j))&1:
                field[i][j] = 1
                cnt += 1
    return field, cnt

def is_included(field):
    for i, j in town_set:
        if not field[i][j]:
            return False
    else:
        return True

def is_connected(field, cnt):
    global seen
    for i in range(4):
        for j in range(4):
            if field[i][j]:
                seen = [[0] * 4 for _ in range(4)]
                c = bfs(field, i, j, 0, 4)
                if c != cnt:
                    return False
                else:
                    return True

def is_holl(field, cnt):
    new_field = []
    for row in field:
        new_field.append([0] + row + [0])
    field = [[0] * 6] + new_field + [[0] * 6]
    global seen
    seen = [[0] * 6 for _ in range(6)]
    c = bfs(field, 0, 0, 1, 6)
    if c + cnt == 36:
        return False
    else:
        return True

def valid(y, x, l):
    return 0<=y<l and 0<=x<l

def bfs(field, i, j, p, l):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    deq = deque()
    deq.append((i, j))
    while deq:
        y, x = deq.popleft()
        seen[y][x] = 1
        for d in range(4):
            nexty = y + dy[d]
            nextx = x + dx[d]
            if not valid(nexty, nextx, l):continue
            if field[nexty][nextx] == p:continue
            if seen[nexty][nextx]:continue
            deq.append((nexty, nextx))
    c = 0
    for i in range(len(seen)):
        for j in range(len(seen[0])):
            if seen[i][j]:
                c += 1
    return c

seen = [[0] * 4 for _ in range(4)]
ans = 0
for bit in range(1<<16):
    field, cnt = create_field(bit)
    if not is_connected(field, cnt):continue
    if not is_included(field):continue
    if is_holl(field, cnt):continue
    ans += 1
print(ans)
