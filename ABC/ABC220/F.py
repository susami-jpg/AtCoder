from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

setrecursionlimit(10**7)
input = stdin.readline

"""
#TLE

def main():
    N = int(input())
    edge = [[] for _ in range(N)]
    for _ in range(N-1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        edge[u].append(v)
        edge[v].append(u)

    dp1 = [[-1]*2 for _ in range(N)]

    def dfs1(v, par=-1):
        if dp1[v][0] != -1 and dp1[v][1] != -1:
            return dp1[v][0], dp1[v][1]
        
        S0 = 0
        S1 = 1
        for child in edge[v]:
            if child == par: continue
            dfs1(child, v)
            S0 += dp1[child][0] + dp1[child][1] #子供の数だけvからchildへの辺の貢献度が増加
            S1 += dp1[child][1]
        dp1[v][0] = S0
        dp1[v][1] = S1
        return S0, S1

    dfs1(0)

    dp2 = [[-1]*2 for _ in range(N)]
    dp2[0][0] = 0
    dp2[0][1] = 0
    def dfs2(v, par=-1):
        acc1 = []
        acc2 = []
        children = []
        for child in edge[v]:
            if child == par:continue
            children.append(child)
            acc1.append(dp1[child][0])
            acc2.append(dp1[child][1])
            
        left1 = [0] + acc1 + [0]
        right1 = [0] + acc1 + [0]
        left2 = [0] + acc2 + [0]
        right2 = [0] + acc2 + [0]
        n = len(left1)
        for i in range(1, n):
            left1[i] += left1[i-1]
            left2[i] += left2[i-1]
            right1[n-i-1] += right1[n-i]
            right2[n-i-1] += right2[n-i]
        #rest = left[i] + right[i+2]
        for i, child in enumerate(children):
            dp2[child][0] = dp2[v][0] + dp2[v][1] + left1[i] + right1[i+2] + left2[i] + right2[i+2]
            dp2[child][1] = dp2[v][1] + left2[i] + right2[i+2] + 1
            dfs2(child, v)
        return

    dfs2(0)

    for i in range(N):
        ans = dp1[i][0] + dp2[i][0] + dp2[i][1]
        print(ans)

if __name__ == "__main__":
    main()
"""
         
         
N = int(input())
edge = [[] for _ in range(N)]
for _ in range(N-1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    edge[v].append(u)
    edge[u].append(v)

dp = [-1] * N 
def dfs1(v, par=-1):
    if dp[v] != -1:
        return dp[v]
    S = 1
    for nextv in edge[v]:
        if nextv == par:continue
        S += dfs1(nextv, v)
    dp[v] = S
    return dp[v]

dfs1(0)
ans = [0] * N
ans[0] = sum(dp[1:])

def dfs2(v, par=-1):
    for nextv in edge[v]:
        if nextv == par:continue
        ans[nextv] = ans[v] - dp[nextv] + (N-dp[nextv])
        dfs2(nextv, v)
    return

dfs2(0)
for i in range(N):
    print(ans[i])
    
