from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
INF = 10**15
MOD = 10**9+7

N, Q = map(int, input().split())
query = []
for _ in range(Q):
    x, y, z, w = map(int, input().split())
    x -= 1
    y -= 1
    z -= 1
    query.append((x, y, z, w))
#bit変換した時の各桁の組み合わせの数
bit_keta = [0] * 60

for d in range(60):
    for i in range(1 << N):
        for x, y, z, w in query:
            # &1しなければ欲しいくらいのbitフラグを取り出せないことに注意
            if ((i>>x)&1)|((i>>y)&1)|((i>>z)&1) != (w>>d)&1:
                break
        else:
            bit_keta[d] += 1

ans = 1
for i in range(60):
    ans *= bit_keta[i]
    ans %= MOD
print(ans)

            