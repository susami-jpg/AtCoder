from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt, factorial
from copy import copy, deepcopy
INF = 10**15
MOD = 998244353

setrecursionlimit(10**7)
N, M, K = map(int, input().split())
A = list(map(int, input().split()))
edge_id = dict()
edge = [[] for _ in range(N)]
for i in range(N-1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    edge[u].append((v, i))
    edge[v].append((u, i))
    edge_id[(u, v)] = i
    edge_id[(v, u)] = i

#dfsは頂点vからスタートしてgoal(t)にたどり着けるかをbool値で返す関数
def dfs(v, par=-1):
    if v == t:
        return True
    for nextv, i in edge[v]:
        if nextv == par:continue
        if dfs(nextv, v):
            cnt[i] += 1
            #nextvからgoalに行けるならvからでもいける(この時にedge[i]を使う)
            return True
    return False

def dfs2(v, par=-1):
    for nextv, i in edge[v]:
        if nextv == par:continue
        prev[nextv] = v
        dfs2(nextv, v)
    return

def reconstruction(t):
    now = t
    while 1:
        nxt = prev[now]
        if nxt == -1:return
        cnt[edge_id[(now, nxt)]] += 1
        now = nxt
    return

cnt = [0] * (N-1)
for i in range(M-1):
    s = A[i]-1
    t = A[i+1]-1
    #dfs(s, par=-1)
    prev = [-1] * N
    dfs2(s)
    reconstruction(t)

#print(cnt)
S = sum(cnt)
R2 = S+K
if R2 < 0 or R2%2:
    exit(print(0))
elif R2 == 0 and S != -K:
    exit(print(0))
R = R2//2
dp = [0] * (R+1)
dp[0] = 1
for i in range(N-1):
    for j in range(R, -1, -1):
        if j+cnt[i] <= R:
            dp[j+cnt[i]] += dp[j]
            dp[j+cnt[i]] %= MOD
    #print(dp)
print(dp[R])
