from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7
"""
N = int(input())
S = [list(input()) for _ in range(N)]
T = [list(input()) for _ in range(N)]
St = [list(x) for x in zip(*S)]
Tt = [list(x) for x in zip(*T)]

for i in range(N):
    if "#" in S[i]:
        Sh = i
        break
for i in range(N-1, -1, -1):
    if "#" in S[i]:
        Seh = i
        break
for i in range(N):
    if "#" in T[i]:
        Th = i
        break
for i in range(N-1, -1, -1):
    if "#" in T[i]:
        Teh = i
        break
for j in range(N):
    if "#" in St[j]:
        Sw = j
        break
for j in range(N-1, -1, -1):
    if "#" in St[j]:
        Sew = j
        break
for j in range(N):
    if "#" in Tt[j]:
        Tw = j
        break
for j in range(N-1, -1, -1):
    if "#" in Tt[j]:
        Tew = j
        break


S = S[Sh:Seh+1]
T = T[Th:Teh+1]
S = [list(x) for x in zip(*S)]
T = [list(x) for x in zip(*T)]
S = S[Sw:Sew+1]
T = T[Tw:Tew+1]

def rotate(T):
    h = len(T)
    w = len(T[0])
    new = [["."] * h for _ in range(w)]
    for i in range(h):
        for j in range(w):
            new[w-1-j][i] = T[i][j]
    return new

for i in range(4):
    if S == T:
        print("Yes")
        exit()
    T = rotate(T)
else:
    print("No")

"""

N = int(input())
S = [list(input()) for _ in range(N)]
T = [list(input()) for _ in range(N)]

def check(s, t):
    si = N
    sj = N
    ti = N
    tj = N
    for i in range(N):
        for j in range(N):
            if s[i][j] == "#":
                si = min(si, i)
                sj = min(sj, j)
            if t[i][j] == "#":
                ti = min(ti, i)
                tj = min(tj, j)
    
    ok = True
    for i in range(N):
        for j in range(N):
            sy = si + i
            sx = sj + j
            if sy < N and sx < N:
                s_chr = s[sy][sx]
            else:
                s_chr = "."
            ty = ti + i
            tx = tj + j
            if ty < N and tx < N:
                t_chr = t[ty][tx]
            else:
                t_chr = "."
            if s_chr != t_chr:
                ok = False
    return ok

def rotate(T):
    h = len(T)
    w = len(T[0])
    new = [['.'] * h for _ in range(w)]
    for i in range(h):
        for j in range(w):
            new[w-1-j][i] = T[i][j]
    return new

ok = check(S, T)
T = rotate(T)
ok |= check(S, T)
T = rotate(T)
ok |= check(S, T)
T = rotate(T)
ok |= check(S, T)

if ok:
    print("Yes")
else:
    print("No")
    








            
