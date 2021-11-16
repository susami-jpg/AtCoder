# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 16:37:52 2021

@author: kazuk
"""

N = int(input())

def agg_func(x, y):
    return x + y

dp1 = [-1] * N
dp2 = [-1] * N

def Rerooting(N, edge, agg_func, ide_ele, mod=1):
    #dp1[v]: 頂点vを含む部分木のooの総数
    #dfs1は帰りがけ順でdp1の計算を行う
        def dfs1(v, par=-1):
            if dp1[v] != -1:
                return dp1[v]

            #ここを総積でとるのか総和でとるのか適宜変更
            for nextv in edge[v]:
                if nextv == par:continue
                dfs1(nextv, v)
                #ここを総積でとるのか総和でとるのか適宜変更
                #S += dp1[nextv]
                ide_ele = agg_func(ide_ele, dp1[nextv])
                ide_ele %= mod
            dp1[v] = ide_ele%mod #dpテーブル更新
            return dp1[v]

        def dfs2(v, par=-1):
            #左右からの子ノードのdp1の値について累積積もしくは累積和をとってvの子ノードのdp2の計算を高速化
            #これは結合則がなりたつこと、単位元が存在するといったモノイドであることが条件
            #ex: 和、積、0を単位元としたGCD、max、minなど
            if par == -1:
                dp2[v] = ide_ele
            
            L = len(edge[v])
            left = [ide_ele] * (L+1)
            right = [ide_ele] * (L+1)
            for i in range(1, L+1):
                child_L = edge[v][i-1]
                child_R = edge[v][L-i]
                left[i] = left[i-1]
                if child_L != par:
                    #ここの累積ooを適宜変更
                    left[i] = agg_func(left[i], dp1[child_L])
                    left[i] %= mod
                right[L-i] = right[L-i+1]
                if child_R != par:
                    #ここの累積ooを適宜変更
                    right[L-i] = agg_func(right[L-i], dp1[child_R])
                    right[L-i] %= mod
                    
            #vの子ノードについてdp2を更新 -> dfs2
            for i, child in enumerate(edge[v]):
                #すでに探索済みならcontinue
                if child == par:continue
                
                #適宜変更
                #restはchild以外のvの子ノードのdp1の値の総oo
                rest = agg_func(left[i], right[i+1])
                
                #行きかけ順なのでdp2[v]は計算済み
                #適宜変更
                dp2[child] = agg_func(rest, dp2[v]) #dp2の更新
                dp2[child] %= mod
                dfs2(child, v) #自分の子についてdfs
            return
        dfs1(0)
        dfs2(0)
        return

#全方位木dp
def main():
    from sys import setrecursionlimit, stdin
    setrecursionlimit(10**7)
    input = stdin.readline
    #modは自分で設定するか入力でもらうか適宜変更
    n, mod = map(int, input().split())
    adj = [[] for _ in range(n)]
    for _ in range(n-1):
        x, y = map(int, input().split())
        adj[x-1].append(y-1)
        adj[y-1].append(x-1)
    
    #dp1[v]: 頂点vを含む部分木のooの総数
    dp1 = [-1] * n
    
    #dfs1は帰りがけ順でdp1の計算を行う
    def dfs1(v, par):
        if dp1[v] != -1:
            return dp1[v]
        
        #ここを総積でとるのか総和でとるのか適宜変更
        prod = 1
        for nextv in adj[v]:
            if nextv == par:continue
            dfs1(nextv, v)
            #ここを総積でとるのか総和でとるのか適宜変更
            prod *= dp1[nextv]
            prod %= mod
        dp1[v] = prod #dpテーブル更新
        return dp1[v]%mod
    
    dfs1(0, -1)
    
    #dp2[v]:　頂点vを含まない親方向の部分木のooの総数(dfs1と逆方向)
    dp2 = [-1] * n
    
    #dfs2は行きかけ順でdp2の計算を行う
    #配るdpで行う(dp2[v]を計算するのではなく、vの子ノードのdp2[c]を計算する)
    
    #親ノードのない根と仮定したノードのdp2は1とする(適宜変更)
    dp2[0] = 1
    
    def dfs2(v, par):
        #左右からの子ノードのdp1の値について累積積もしくは累積和をとってvの子ノードのdp2の計算を高速化
        #これは結合則がなりたつこと、単位元が存在するといったモノイドであることが条件
        #ex: 和、積、0を単位元としたGCD、max、minなど
        
        L = len(adj[v])
        left = [1] * (L+1)
        right = [1] * (L+1)
        for i in range(1, L+1):
            child_L = adj[v][i-1]
            child_R = adj[v][L-i]
            left[i] = left[i-1]
            if child_L != par:
                #ここの累積ooを適宜変更
                left[i] *= dp1[child_L]
                left[i] %= mod
            right[L-i] = right[L-i+1]
            if child_R != par:
                #ここの累積ooを適宜変更
                right[L-i] *= dp1[child_R]
                right[L-i] %= mod
                
        #vの子ノードについてdp2を更新 -> dfs2
        for i, child in enumerate(adj[v]):
            #すでに探索済みならcontinue
            if child == par:continue
            
            #適宜変更
            #restはchild以外のvの子ノードのdp1の値の総oo
            rest = left[i] * right[i+1]
            
            #行きかけ順なのでdp2[v]は計算済み
            dp2[child] = rest * dp2[v] + 1 #dp2の更新
            dp2[child] %= mod
            dfs2(child, v) #自分の子についてdfs
        return
    
    dfs2(0, -1)
    
    
    #最後に求められる解を各頂点について出力
    #適宜変更
    for v in range(n):
        ans = (dp1[v]-1) * dp2[v]
        ans %= mod
        print(ans)

if __name__ == "__main__":
    main()
