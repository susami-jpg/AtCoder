from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right
from math import sqrt
INF = 10**15
MOD = 998244353

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

AB = list(zip(A, B))
AB.sort()

#dp[i][j][k]でやるとTLE
#dp[k][i][j]にしたらAC(配列の外側を軽くすると早くなるS)
#dp[k][i][j]:= i番目までで和がjになるような場合の数(k=Trueならi番目を使い、k=Falseならi番目を使わない)
dp = [[[0] * 5001 for _ in range(N)] for _ in range(2)]

#dp初期化
a, b = AB[0]
dp[0][0][0] = 1
dp[1][0][b] = 1

#今回求めるべきものは各i,jについてj <= A[i] and k=Trueとなるものの総和
ans = 0

#配るdp
for i in range(N):
    for j in range(5001):
        #ansを数えるパート
        a, b = AB[i]
        if j <= a:
            ans += dp[1][i][j]
            ans %= MOD
        
        #dp更新パート
        if i == N-1:continue
        a, b = AB[i+1]
        #i+1番目を使わない場合
        dp[0][i+1][j] += dp[0][i][j] + dp[1][i][j]
        dp[0][i+1][j] %= MOD

        #i+1番目を使う場合
        if j + b > 5000:continue
        dp[1][i+1][j+b] += dp[0][i][j] + dp[1][i][j]
        dp[1][i+1][j+b] %= MOD
    
print(ans)



