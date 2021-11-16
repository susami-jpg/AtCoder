from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

H, W, A, B = map(int, input().split())
setrecursionlimit(10**7)
ans = 0
def dfs(i, j, used, a, b):
    global ans
    if i == H-1 and j == W-1 and a == 0 and b == 0:
        ans += 1
        return
    n = W*i + j
    if (used>>n)&1:
        if j+1 < W:
            dfs(i, j+1, used, a, b)
        else:
            dfs(i+1, 0, used, a, b)
    else:
        if a and i+1 < H and (used>>(W*(i+1) + j))&1 == 0:
            if j+1 < W:
                dfs(i, j+1, used|(1<<(W*(i+1)+j)), a-1, b)
            else:
                dfs(i+1, 0, used|(1<<(W*(i+1)+j)), a-1, b)
        
        if a and j+1 < W and (used>>(W*i + j+1))&1 == 0:
            dfs(i, j+1, used|(1<<(W*i + j+1)), a-1, b)
            
        if b:
            dfs(i, j, used|(1<<n), a, b-1)

dfs(0, 0, 0, A, B)
print(ans)


        
    