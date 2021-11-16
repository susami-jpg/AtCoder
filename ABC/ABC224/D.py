from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt, factorial
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7
"""
N = 9
M = int(input())
edge = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    edge[u].append(v)
    edge[v].append(u)

P = list(map(int, input().split()))
#9を駒のない頂点とする  
s = [9] * N
for j in range(8):
    s[P[j]-1] = j+1
empty = s.index(9)
s = tuple(s)

def decode(v):
    return list(map(int, list(str(v))))

def encode(v):
    return int("".join(list(map(str, v))))

ok = [i for i in range(1, 10)]
seen = dict()
deq = deque()
deq.append((s))
seen[s] = 0
cnt = 0
while deq:
    v = deq.popleft()
    d = seen[v]
    v = list(v)
    empty = v.index(9)
    #print(seen)
    for f in edge[empty]:
        v[f], v[empty] = v[empty], v[f]
        if tuple(v) not in seen:
            nextv = tuple(v)
            seen[nextv] = d + 1
            deq.append((nextv))
        v[f], v[empty] = v[empty], v[f]

ans=(1,2,3,4,5,6,7,8,9)
print(seen[ans] if ans in seen else -1)
"""

from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt, factorial
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

N = 9
M = int(input())
edge = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    edge[u].append(v)
    edge[v].append(u)

P = list(map(int, input().split()))
#9を駒のない頂点とする  
s = [9] * N
for j in range(8):
    s[P[j]-1] = j+1

def decode(v):
    return list(map(int, list(str(v))))

def encode(v):
    return int("".join(list(map(str, v))))

ok = [i for i in range(1, 10)]
#print(ok)
seen = dict()
deq = deque()
deq.append(encode(s))
seen[encode(s)] = 0
cnt = 0
while deq:
    v = deq.popleft()
    v = decode(v)
    empty = v.index(9)
    d = seen[encode(v)]
    if v == ok:
        print(d)
        exit()
    #print(seen)
    for f in edge[empty]:
        v[f], v[empty] = v[empty], v[f]
        if encode(v) not in seen:
            seen[encode(v)] = d+1
            deq.append(encode(v))
        v[f], v[empty] = v[empty], v[f]
else:
    print(-1)
    