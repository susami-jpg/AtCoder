from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right
from math import sqrt
INF = 10**15
MOD = 10**9+7

N, M = map(int, input().split())
const = [tuple(map(int, input().split())) for _ in range(M)]

for n in range(1000):
    ns = str(n)
    if len(ns) != N:continue
    for s, c in const:
        s -= 1
        if int(ns[s]) != c:
            break
    else:
        print(n)
        exit()
else:
    print(-1)
