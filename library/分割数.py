# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 10:23:52 2021

@author: kazuk
"""

#分割数
"""
P(n, k) = P(n, k-1) + P(n-k, k)
の導出です。n を k 個の 0 以上の整数の和へと分割する方法のうち

0 を含むもの:
0 が何個あるかはわからないが、そのうちの 1 個の 0 を取り除いてしまってもよくて、残りの k - 1 個の 0 以上の整数の和で n を表す方法を考えればよい。よって、P(n, k-1) 通り。

0 を含まないもの:
n を k 個の 1 以上の整数に分割する場合の数、つまり Q(n, k) なので、P(n-k, k) 通り。 　

以上より、P(n, k) = P(n, k-1) + P(n-k, k) が成立します。
一瞬、前者の場合について、0 が複数ある場合にダブルカウントしてしまってそうで怖くなるのですが、今回は k 個の整数は区別できないので大丈夫です。
"""

#再帰による実装
def part_num(n, k):
    if n == 1 or k == 1:
        return 1
    if n < 0 or k < 1:
        return 0
    else:
        return part_num(n - k, k) + part_num(n, k - 1)

def partition_number(n):
    return part_num(n, n)


#動的計画法によるアルゴリズム：
#O(NK)
#二次元配列 p を用意して 0 で初期化する
#p(n, k) = 1                          ; n = 0 または k = 1
#p(n, k) = 0                          ; n < 0 または k < 1
#p(n, k) = p(n - k, k) + p(n, k - 1)
#modが必要ないときはとる/p(0, 0)を特殊化したいときも注意
def part_num(n, k):
    if n == k == 0:
        return 1
    mod = 10**9 + 7
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    for j in range(1, k+1):
        dp[0][j] = 1
    for i in range(1, n+1):
        for j in range(1, k+1):
            if i - j >= 0:
                dp[i][j] = (dp[i][j-1] + dp[i-j][j])%mod
            else:
                dp[i][j] = dp[i][j-1]
                
    return dp[n][k]


#分割数 (動的計画法による高速化)
def partition_number2(n):
    table = [1] * (n + 1)
    for k in range(2, n + 1):
        for m in range(k, n + 1):
            table[m] += table[m - k]
    return table[n]



#分割数 (オイラーの五角数定理/さらなる高速化)
# 五角数
def pentagon(n): return n * (3 * n - 1) / 2

def partition_number3(n):
    p = [0] * (n + 1)
    p[0] = 1
    for i in range(1, n + 1):
        j = 1
        s = 1
        while True:
            k = pentagon(j)
            if i < k: break
            p[i] += p[i - k] * s
            k = pentagon(-j)
            if i < k: break
            p[i] += p[i - k] * s
            j += 1
            s *= -1
    return p[n]


#分割したリストを返す関数
def part_int_sub(n, k, a):
    if n == 0:   print (a)
    elif n == 1: print (a + [1])
    elif k == 1: print (a + [1] * n)
    else:
        if n >= k:
            part_int_sub(n - k, k, a + [k])
        part_int_sub(n, k - 1, a)

def partition_of_int(n): part_int_sub(n, n, [])



#奇数で分割したときの分割数

def part_num_odd(n, k):
    if n == 1 or k == 1:
        return 1
    if n < 0 or k < 1:
        return 0
    else:
        return part_num_odd(n - k, k) + part_num_odd(n, k - 2)

def partition_number_odd(n):
    if n % 2 == 0:
        return part_num_odd(n, n - 1)
    return part_num_odd(n, n)



#奇数で分割したときの分割数 (2)

def partition_number_odd2(n):
    table = [1] * (n + 1)
    for k in range(3, n + 1, 2):
        for m in range(k, n + 1):
            table[m] += table[m - k]
    return table[n]



#奇数で分割する

def part_int_odd_sub(n, k, a):
    if n == 0:   print (a)
    elif n == 1: print (a + [1])
    elif k == 1: print (a + [1] * n)
    else:
        if n >= k:
            part_int_odd_sub(n - k, k, a + [k])
        part_int_odd_sub(n, k - 2, a)

def partition_of_int_odd(n):
    if n % 2 == 0:
        part_int_odd_sub(n, n - 1, [])
    else:
        part_int_odd_sub(n, n, [])