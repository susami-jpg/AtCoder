from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

s = input()
t = input()
S = len(s)
T = len(t)

char = defaultdict(list)
for i in range(S):
    a = ord(s[i])-97
    char[a].append(i+1)

now = 0
rotate = 0

def More(K: int, A: list) -> int:
    '配列Aの中のうち、kより大きいものの個数と始まりの0indexを返すライブラリ'
    '-1の時は解が無い時'
    ans = bisect_right(A, K)
    l = len(A)
    return l - ans, (ans if ans <= l - 1 else -1)

for i in range(T):
    a = ord(t[i])-97
    if len(char[a]) == 0:
        print(-1)
        exit()
    k, ind = More(now, char[a])
    if ind == -1:
        rotate += 1
        now = char[a][0]
    else:
        now = char[a][ind]
print(rotate*S + now)


    