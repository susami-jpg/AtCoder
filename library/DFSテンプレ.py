# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 12:51:04 2021

@author: kazuk
"""
#ALDS1 DFS
N = int(input())
adj = [[] for i in range(N)]
for n in range(N):
    V = list(map(int, input().split()))
    for v in V[2:]: # u,k,v1,v2,...
        adj[n].append(v-1)
d = [0] * N # 発見時刻
f = [0] * N # 完了時刻

def dfs(v, t):
    t+=1 # 発見したらインクリメント
    d[v] = t
    for next in adj[v]:
        if d[next] == 0: # 未発見なら
            t = dfs(next, t)
    t+=1 # 完了してもインクリメント
    f[v] = t
    return t

t = 0
for n in range(N):
    if d[n]==0: # 未発見なら
        t = dfs(n,t)
    print (n+1,d[n],f[n])




#薄氷渡り
dxdy = ((0,1),(0,-1),(1,0),(-1,0))
M = int(input())
N = int(input())

mp = []
mp.append([0]*(M+2))
for n in range(N):
    line = list(map(int, input().split()))
    mp.append([0]+line+[0])
mp.append([0]*(M+2))

ans = 0
def dfs(n,m,d):
    global ans # グローバル変数
    if mp[n][m] == 0:
        return
    if ans < d:
        ans = d
    
    mp[n][m] = 0
    for dx, dy in dxdy:
        next_n = n + dy
        next_m = m + dx
        dfs(next_n, next_m, d+1)
    mp[n][m] = 1
