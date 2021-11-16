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

S = list(input())
K = int(input())
N = len(S)
v = []
for s in S:
    if s == "K":
        v.append(1)
    elif s == "E":
        v.append(2)
    else:
        v.append(3)

def encode(v):
    v = list(map(str, v))
    return int("".join(v))

def decode(v):
    return list(map(int, list(str(v))))
             
deq = deque()
deq.append(tuple(v))
dist = dict()
dist[encode(v)] = 0
ans = 1
while deq:
    v = list(deq.popleft())
    prev = encode(v)
    for i in range(1, N):
        v[i-1], v[i] = v[i], v[i-1]
        if encode(v) not in dist and dist[prev] + 1 <= K:
            deq.append(tuple(v))
            ans += 1
            dist[encode(v)] = dist[prev] + 1
        v[i-1], v[i] = v[i], v[i-1]
print(ans)
