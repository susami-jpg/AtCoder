from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt, factorial
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7


#トポロジカルソート
from collections import deque

def topological_sort():
    def chmax(a, b):
        if a >= b:
            return a
        else:
            return b
        
    n, m = map(int, input().split())
    edge = [[] for _ in range(n)]
    
    #各頂点の入力辺の本数を記録
    deg = [0] * n
    for _ in range(m):
        x, y = map(int, input().split())
        edge[x - 1].append(y - 1)
        deg[y - 1] += 1
    
    #入力辺を持たない頂点をqueueにいれる
    hq = []
    for v in range(n):
        if deg[v] == 0:
            heappush(hq, v)
    
    #各頂点の最初に入力辺を持たなかった点からの距離
    dp = [0] * n
    topo = []
    #queに同時に複数のノードが入っている瞬間があると、pop時にどれが選ばれるかによってソート結果が変わる。
    #よってqueに複数のノードが入っている瞬間がある=複数のトポロジカルソートがあると判定できる
    #ここで、例えばqueに優先度キューを用いるとノードIDが小さい順に取り出され、小さいノードを優先して前に持ってくるよう固定される。
    while hq:
        v = heappop(hq)
        topo.append(v+1)
        for nextv in edge[v]:
            #辺(v, nextv)をグラフから削除する
            deg[nextv] -= 1
            if deg[nextv] == 0:
                heappush(hq, nextv)
            #最初に入力辺を持たなかった点からの距離
            dp[nextv] = chmax(dp[nextv], dp[v] + 1)
    
    #閉路の場合-1を返す
    if len(topo) != n:
        return -1
    else:
        return topo


ans = topological_sort()
if ans == -1:
    print(ans)
else:
    print(*ans)
    
