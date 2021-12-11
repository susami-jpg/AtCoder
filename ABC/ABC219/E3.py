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

setrecursionlimit(10**7)
A = [list(map(int, input().split())) for _ in range(4)]

def valid(y, x):
    return 0 <= y < 5 and 0 <= x < 5

used = [[0] * 5 for _ in range(5)]
in_out = [[0] * 4 for _ in range(4)]
ans = 0
def dfs(y, x, sy, sx):
    global ans
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    if used[sy][sx] and sy==y and sx==x:
        acc_in_out = flip(in_out)
        if check(acc_in_out):
            ans += 1
        return

    used[y][x] = 1
    for d in range(4):
        nexty = y + dy[d]
        nextx = x + dx[d]
        if not valid(nexty, nextx):continue
        if (nexty, nextx) != (sy, sx) and used[nexty][nextx]:continue
        if nextx == x and x < 4:
            my = min(nexty, y)
            #print(my, nextx)
            in_out[my][nextx] += 1
            dfs(nexty, nextx, sy, sx)
            in_out[my][nextx] -= 1
        else:
            dfs(nexty, nextx, sy, sx)
    used[y][x] = 0
    return

def flip(in_out):
    acc_in_out = []
    for row in in_out:
        row = list(accumulate(row))
        #print(row)
        acc_in_out.append(row)
    #print("##################")
    return acc_in_out

def check(acc_in_out):
    for i in range(4):
        for j in range(4):
            if A[i][j] and A[i][j] != acc_in_out[i][j]%2:
                return False
    return True

for i in range(4):
    for j in range(4):
        dfs(i, j, i, j)
        used[i][j] = 1
print(ans//2)

