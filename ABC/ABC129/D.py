from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

def LessThan(K: int, A: list) -> int:
    '配列Aの中のうち、k未満の個数と終わりの0indexを返すライブラリ'
    '-1の時は解が無い時'
    ans = bisect_left(A, K)
    return ans, (-1 if ans == 0 else ans - 1)

H, W = map(int, input().split())
maze = []
for _ in range(H):
    maze.append("#" + input() + "#")
maze = ["#" * (W+2)] + maze + ["#" * (W+2)]

blockH = [[] for _ in range(H+2)]
blockW = [[] for _ in range(W+2)]
for i in range(H+2):
    for j in range(W+2):
        if maze[i][j] == "#":
            blockH[i].append(j)
            blockW[j].append(i)

ans = 0
for i in range(1, H+1):
    for j in range(1, W+1):
        if maze[i][j] == "#":continue
        cnt = 0
        _, ind = LessThan(j, blockH[i])
        cnt += blockH[i][ind+1] - blockH[i][ind] - 1
        _, ind = LessThan(i, blockW[j])
        cnt += blockW[j][ind+1] - blockW[j][ind] - 1
        cnt -= 1
        ans = max(ans, cnt)

print(ans)
