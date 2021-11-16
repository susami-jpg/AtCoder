from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt, factorial
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

setrecursionlimit(10**7)
N = int(input())
edge = [[] for _ in range(N)]
P = list(map(int, input().split()))
for i, p in enumerate(P):
    #edge[i].append(p)
    edge[p-1].append(i+1)

time = 0
in_time = [-1] * N
out_time = [-1] * N
depth = [-1] * N

def dfs(v, d, par=-1):
    global time
    in_time[v] = time
    depth[v] = d
    time += 1
    max_in_time = in_time[v]
    for nextv in edge[v]:
        if nextv == par:continue
        dfs(nextv, d+1, v)
        #in_time[nextv]とmaxをとると間違い
        #in_timeでmaxをとると自分の孫以降のin_timeまでmaxを獲ることはできない
        #out_time[nextv]とmaxをとる
        max_in_time = max(max_in_time, out_time[nextv])
    out_time[v] = max_in_time
    #out_time[v] = time
    return

dfs(0, 0)

depth_rec = defaultdict(list)
for v, d in enumerate(depth):
    depth_rec[d].append(in_time[v])

for val in depth_rec.values():
    val.sort()



def OrLessThan(K: int, A: list) -> int:
    '配列Aの中のうち、k以下の個数と終わりの0indexを返すライブラリ'
    '-1の時は解が無い時'
    ans = bisect_right(A, K)
    return ans, (-1 if ans == 0 else ans - 1)

def LessThan(K: int, A: list) -> int:
    '配列Aの中のうち、k未満の個数と終わりの0indexを返すライブラリ'
    '-1の時は解が無い時'
    ans = bisect_left(A, K)
    return ans, (-1 if ans == 0 else ans - 1)

#ans1 = []
Q = int(input())
for i in range(Q):
    u, d = map(int, input().split())
    u -= 1
    left = in_time[u]
    right = out_time[u]
    k_r, _ = OrLessThan(right, depth_rec[d])
    k_l, _ = LessThan(left, depth_rec[d])
    print(k_r - k_l)


"""
葉からdp解
setrecursionlimit(10**7)
N = int(input())
edge = [[] for _ in range(N)]
P = list(map(int, input().split()))
for i, p in enumerate(P):
    #edge[i].append(p)
    edge[p-1].append(i+1)

Q = int(input())
q = defaultdict(list)
query = []
for _ in range(Q):
    u, d = map(int, input().split())
    u -= 1
    q[u].append(d)
    query.append((u, d))

in_rec = defaultdict(int)
out_rec = defaultdict(int)
depth = [0] * (2 * 10**5 + 1)
def dfs(v, d, depth, par=-1):
    if len(q[v]):
        for dist in q[v]:
            in_rec[(v, dist)] = depth[dist]
    depth[d] += 1
    for nextv in edge[v]:
        if nextv == par:continue
        dfs(nextv, d+1, depth, v)
    if len(q[v]):
        for dist in q[v]:
            out_rec[(v, dist)] = depth[dist]
    return

dfs(0, 0, depth)
for u, d in query:
    print(out_rec[(u, d)] - in_rec[(u, d)])
    
"""




from sys import setrecursionlimit
from bisect import bisect_left, bisect_right
setrecursionlimit(10**7)
n = int(input())
adj = [[] for _ in range(n)]
p = list(map(int, input().split()))
for v, par in enumerate(p):
    adj[par - 1].append(v + 1)

#ある深さのノード(行きかけ順の番号で記録)のリスト
depth = [[] for _ in range(n)]
seen = [0] * n
#頂点vの部分木を行きかけ順のリストで記録
segment = [[0, 0] for _ in range(n)]

def dfs(v, d, e):
    seen[v] = 1
    segment[v][0] = e
    depth[d].append(e)
    for nextv in adj[v]:
        if seen[nextv] == 0:
            e = dfs(nextv, d + 1, e + 1)
    segment[v][1] = e
    return e

dfs(0, 0, 0)

q = int(input())
ans2 = []
for i in range(q):
    u, d = map(int, input().split())
    cnd = depth[d]
    left = bisect_left(cnd, segment[u-1][0])
    right = bisect_right(cnd, segment[u-1][1])
    ans2.append((i, right - left))
print(*ans2)
    
"""
27
1 1 1 2 2 3 4 4 4 5 6 6 7 9 9 9 10 11 12 12 13 14 15 16 16 21
21
1 3
2 2
3 4
4 2
4 3
5 2
5 3
6 4
7 4
7 6
8 2
8 3
9 3
9 4
10 3
12 5
12 4
13 4
16 4
21 5
21 6
"""

#global変数timeでout_timeの更新を行う場合
#out_timeの値がout_timeを子のin_timeの最大値とする場合より1大きくなる
#よってorLessではなくLessをつかう
from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt, factorial
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

setrecursionlimit(10**7)
N = int(input())
edge = [[] for _ in range(N)]
P = list(map(int, input().split()))
for i, p in enumerate(P):
    #edge[i].append(p)
    edge[p-1].append(i+1)

time = 0
in_time = [-1] * N
out_time = [-1] * N
depth = [-1] * N

def dfs(v, d, par=-1):
    global time
    in_time[v] = time
    depth[v] = d
    time += 1
    #max_in_time = in_time[v]
    for nextv in edge[v]:
        if nextv == par:continue
        dfs(nextv, d+1, v)
        #in_time[nextv]とmaxをとると間違い
        #in_timeでmaxをとると自分の孫以降のin_timeまでmaxを獲ることはできない
        #out_time[nextv]とmaxをとる
        #max_in_time = max(max_in_time, out_time[nextv])
    #out_time[v] = max_in_time
    out_time[v] = time
    return

dfs(0, 0)

depth_rec = defaultdict(list)
for v, d in enumerate(depth):
    depth_rec[d].append(in_time[v])

for val in depth_rec.values():
    val.sort()



def OrLessThan(K: int, A: list) -> int:
    '配列Aの中のうち、k以下の個数と終わりの0indexを返すライブラリ'
    '-1の時は解が無い時'
    ans = bisect_right(A, K)
    return ans, (-1 if ans == 0 else ans - 1)

def LessThan(K: int, A: list) -> int:
    '配列Aの中のうち、k未満の個数と終わりの0indexを返すライブラリ'
    '-1の時は解が無い時'
    ans = bisect_left(A, K)
    return ans, (-1 if ans == 0 else ans - 1)

#ans1 = []
Q = int(input())
for i in range(Q):
    u, d = map(int, input().split())
    u -= 1
    left = in_time[u]
    right = out_time[u]
    k_r, _ = LessThan(right, depth_rec[d])
    k_l, _ = LessThan(left, depth_rec[d])
    print(k_r - k_l)
