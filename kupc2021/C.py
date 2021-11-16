from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt, factorial
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
rec = []
for i in range(N):
    rec.append((A[i], 0, i))
    rec.append((B[i], 1, i))
rec.sort()
money = 0
passed_gacha = 0
min_gacha = INF
ans = 0
now = 0
for x, val, i in rec:
    ans += x-now
    now = x
    if val:
        money += 1
        #通り過ぎたガチャを引けるだけのコインがあつまったら
        if passed_gacha and money == passed_gacha:
            #戻ってガチャする
            ans += now-min_gacha
            now = min_gacha
            money = 0
            passed_gacha = 0
            min_gacha = INF
    else:
        if money:
            money -= 1
        else:
            passed_gacha += 1
            min_gacha = min(min_gacha, x)
    if val == 0 and i == N-2:
        break

if passed_gacha == 0:
    if B[-1] > A[-1]:
        ans += abs(B[-1]-now) + abs(B[-1]-A[-1])
    else:
        ans += abs(A[-1]-now)
    exit(print(ans))
else:
    if A[-1] >= B[-1]:
        lim = A[-1]
        last = 0
    else:
        lim = B[-1]
        last = 1
    ans1 = ans + abs(lim-now) + abs(lim-min_gacha)
    ans2 = ans + abs(B[-2]-now) + abs(B[-2]-min_gacha) + abs(min_gacha-lim)
    if last:
        ans2 += abs(A[-1]-B[-1])
    print(min(ans1, ans2))
        
