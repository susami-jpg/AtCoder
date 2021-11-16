# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 16:37:41 2021

@author: kazuk
"""

#前から見る
def solve(S, T):
    S = " " + S
    T = " " + T
    L1 = len(S)
    L2 = len(T)
    dp = [[0] * L2 for i in range(L1)]

    for i in range(1, L1):
        for j in range(1, L2):
            r = max(dp[i - 1][j], dp[i][j - 1])
            if S[i] == T[j]:
                r = max(r, dp[i - 1][j - 1] + 1)
            dp[i][j] = r
    # dp[-1][-1] が長さの解

    # ここからは復元処理
    res = []
    i = L1-1; j = L2-1
    while i > 0 and j > 0:
        if S[i] == T[j]:
            res.append(S[i])
            i -= 1; j -= 1
        if dp[i][j] == dp[i - 1][j]:
            i -= 1
        elif dp[i][j] == dp[i][j - 1]:
            j -= 1
    return "".join(res[::-1])

print(solve("asdcsascsadsd", "assdcascdascasca"))

#後ろから見る
def solve(S, T):
    L1 = len(S)
    L2 = len(T)
    dp = [[0] * (L2 + 1) for i in range(L1 + 1)]

    for i in range(L1 - 1, -1, -1):
        for j in range(L2 - 1, -1, -1):
            r = max(dp[i + 1][j], dp[i][j + 1])
            if S[i] == T[j]:
                r = max(r, dp[i + 1][j + 1] + 1)
            dp[i][j] = r
    # dp[0][0] が長さの解

    # ここからは復元処理
    res = []
    i = 0; j = 0
    while i < L1 and j < L2:
        if S[i] == T[j]:
            res.append(S[i])
            i += 1; j += 1
        elif dp[i][j] == dp[i + 1][j]:
            i += 1
        elif dp[i][j] == dp[i][j + 1]:
            j += 1
    return "".join(res)

print(solve("asdcsascsadsd", "assdcascdascasca"))


#連続のみの場合
def solve(S, T):
    L = len(S)
    M = len(T)
    
    ma = 0
    dp = [[0] * M for _ in range(L)]
    for i in range(L):
        for j in range(M):
            if S[i] == T[j]:
                if i-1<0 or j-1<0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j-1] + 1
            ma = max(dp[i][j], ma)
    return ma

S = input()
T = input()
print(solve(S, T))


s = input()
t = input()
n = len(s)
a = i = 0
j = 1
while i + j <= n:
    if s[i:i + j] in t:
        a = j
        j += 1
    else:
        i += 1
print(a)