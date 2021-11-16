from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = list(input())
game_hand = []
for c in T:
    if c == "r":
        game_hand.append(0)
    elif c == "s":
        game_hand.append(1)
    else:
        game_hand.append(2)

hand = ""
point = [R, S, P]
win_hand = {0: 2, 1: 0, 2: 1}
get_point = [-1] * N

for i in range(N):
    if get_point[i] != -1:continue
    my_hand = win_hand[game_hand[i]]
    get_point[i] = point[my_hand]
    now = i+K
    prev_hand = my_hand
    while now < N:
        my_hand = win_hand[game_hand[now]]
        if my_hand == prev_hand:
            get_point[now] = 0
            prev_hand = None
        else:
            get_point[now] = point[my_hand]
            prev_hand = my_hand
        now += K

ans = sum(get_point)
print(ans)