from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right
from math import sqrt
INF = 10**15
MOD = 10**9+7

N, M = map(int, input().split())
#現在取り出せる色の番号を保持する配列
stack = []
#各色について筒の一番上にある場合にその筒の番号を保持する配列
color = [[] for _ in range(N+1)]
pipes = []
for i in range(M):
    k = int(input())
    A = list(map(int, input().split()))[::-1]
    top_col = A.pop()
    pipes.append(A)
    color[top_col].append(i)
    if len(color[top_col]) == 2:
        stack.append(top_col)

cnt = 0
while stack:
    #現在取り出せる色を取り出す(現在取り出せる物ならどの順でもよい)
    c = stack.pop()
    cnt += 1
    x, y = color[c]
    if len(pipes[x]):
        nxt_col = pipes[x].pop()
        color[nxt_col].append(x)
        if len(color[nxt_col]) == 2:
            stack.append(nxt_col)
    if len(pipes[y]):
        nxt_col = pipes[y].pop()
        color[nxt_col].append(y)
        if len(color[nxt_col]) == 2:
            stack.append(nxt_col)

if cnt == N:
    print("Yes")
else:
    print("No")


    