# -*- coding: utf-8 -*-
"""
Created on Mon May 10 15:03:36 2021

@author: kazuk
"""

#配列Aの連続部分列の和がK以下となるような(i, j)の組の個数を数える
def syakutori1(A, K):
    A = [0] + A
    n = len(A)
    r = 0
    S = 0
    ans = 0
    for l in range(n-1):
        while r+1 < n and S + A[r+1] <= K:
            S += A[r+1]
            r += 1
        ans += r-l
        S -= A[l+1]
    return ans

#配列Aの連続部分列の和がKより大きくなるような(i, j)の組の個数を数える
def syakutori2(A, K):
    A = [0] + A
    n = len(A)
    r = 0
    S = 0
    ans = 0
    for l in range(n-1):
        while r+1 < n and S + A[r+1] <= K:
            S += A[r+1]
            r += 1
        #nは1indexにするための調整である[0]を含んだ数(もとの配列の長さ+1)になっているので-1する
        ans += n-1-r
        S -= A[l+1]
    return ans

#合計がK以下である範囲の最大長を求める
def syakutori3(A, K):
    ans = 0
    A = [0] + A
    n = len(A)
    r = 0
    S = 0
    for l in range(n-1):
        while r+1 < n and S + A[r+1] <= K:
            S += A[r+1]
            r += 1
        ans = max(ans, r-l)
    return ans

#合計がKより大きいような範囲の最小長を求める
def syakutori4(A, K):
    INF = 10**15
    A = [0] + A
    n = len(A)
    r = 0
    S = 0
    ans = n+1
    for l in range(n-1):
        while r+1 < n and S + A[r+1] <= K:
            S += A[r+1]
            r += 1
            print(r)
        S -= A[l+1]
        ans = min(ans, r+1-l)
    return ans


A = [3, 2, 1, 5, 7, 9, 11, 2, 1, 3, 20, 5]
print(syakutori3(A, 25))
print(syakutori4(A, 25))


#累積積がKを超えないような範囲の最大長を求める
def syakutori5(A, K):
    N = len(A)
    r = 0
    prod = 1
    ans = 0
    #[l, r)
    for l in range(N):
        while r < N and prod * A[r] <= K:
            prod *= A[r]
            r += 1
        ans = max(ans, r-l)
        #lがrを追い越さないように調整
        if r == l:
            r += 1
        #l < rなら今見ていた左端をグループから出す
        else:
            prod //= A[l]
    print(ans)

