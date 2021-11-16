from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt, factorial
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

H, W, C = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
calc_A = [[0] * W for _ in range(H)]
for i in range(H):
    for j in range(W):
        calc_A[i][j] = A[i][j] - C*(i+j)

def acc_min(kingdam):
    new_kingdam = [[0] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            new_kingdam[i][j] = kingdam[i][j]
    for i in range(H):
        for j in range(1, W):
            new_kingdam[i][j] = min(new_kingdam[i][j], new_kingdam[i][j-1])
    for i in range(1, H):
        for j in range(W):
            new_kingdam[i][j] = min(new_kingdam[i][j], new_kingdam[i-1][j])
    return new_kingdam

def get_min(accA):
    res = INF
    for i in range(H):
        for j in range(W):
            rest_min = INF
            if i-1 >= 0:
                rest_min = min(rest_min, accA[i-1][j])
            if j-1 >= 0:
                rest_min = min(rest_min, accA[i][j-1])
            res = min(res, A[i][j] + C*(i+j) + rest_min)
    return res

ans = INF
acc_A = acc_min(calc_A)
ans = min(ans, get_min(acc_A))

new_A = []
for row in A:
    new_A.append(row[::-1])
A = new_A
calc_A = [[0] * W for _ in range(H)]
for i in range(H):
    for j in range(W):
        calc_A[i][j] = A[i][j] - C*(i+j)
acc_A_flip = acc_min(calc_A)
ans = min(ans, get_min(acc_A_flip))
print(ans)
