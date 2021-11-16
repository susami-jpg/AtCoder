from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt, factorial
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

N, M = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if i == 0 and j == 0:continue
        elif i-1 >= 0 and B[i-1][j] + 7 != B[i][j]:
            print("No")
            exit()
        elif j-1 >= 0 and (B[i][j-1] + 1 != B[i][j] or (B[i][j-1]%7==0 and B[i][j]%7 != 0)):
            print("No")
            exit()
print('Yes')
