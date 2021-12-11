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

N, M = map(int, input().split())
N *= 2
A = [input() for _ in range(N)]
d = {"G": 0, "C": 1, "P": 2}
def battle(x, y, i):
    x_te = d[A[x][i]]
    y_te = d[A[y][i]]
    if x_te == y_te:
        return 0, -1
    elif x_te < y_te:
        if x_te == 0 and y_te == 2:
            return  1, y
        else:
            return 1, x
    else:
        if x_te == 2 and y_te == 0:
            return 1, x
        else:
            return 1, y
    
rank = [[0, i] for i in range(N)]
for i in range(M):
    new_rank = []
    for j in range(N//2):
        win_x, x = rank[2*j]
        win_y, y = rank[2*j+1]
        p, winner = battle(x, y, i)
        if p == 0:
            new_rank.append([win_x, x])
            new_rank.append([win_y, y])
        else:
            if winner == x:
                new_rank.append([win_x-1, x])
                new_rank.append([win_y, y])
            else:
                new_rank.append([win_y-1, y])
                new_rank.append([win_x, x])
    new_rank.sort()
    rank = new_rank

for _, id in rank:
    print(id+1)
        
