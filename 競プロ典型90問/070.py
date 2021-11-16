from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right
from collections import defaultdict, deque
from heapq import heappop, heappush, heapify
from math import sqrt
INF = 10**15
MOD = 10**9+7

N = int(input())
X = []
Y = []
plants = []
for i in range(N):
    x, y = map(int, input().split())
    plants.append((x, y))
    X.append((x))
    Y.append((y))

X.sort()
Y.sort()
if N%2:
    px = X[N//2]
    py = Y[N//2]
else:
    px = (X[N//2-1] + X[N//2])/2
    py = (Y[N//2-1] + Y[N//2])/2



ans = 0
for i in range(N):
    x, y = plants[i]
    ans += abs(px-x) + abs(py-y)
print(int(ans))