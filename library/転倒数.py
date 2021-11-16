# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 16:29:48 2021

@author: kazuk
"""

"""
BITを行った後の数列は昇順になるので注意！
具体的な例でイメージすると、 
{3,10,1,8,5}
  のような数列を昇順にソートする時、「正しい順序になっていないペアの数」のことである。

これは、隣り合う2数の交換を繰り返すことでソートするバブルソートにおいて、その必要な最小回数と一致する。

例の場合、 
(3,1)(10,1)(10,8)(10,5)(8,5)
  の5つの組で、左にある数字が右より大きくなっているので、転倒数は5である。
"""
import copy

def BIT(A: list) -> int:
    "転倒数を求める"
    cnt = 0
    n = len(A)
    if n > 1:
        A1 = A[: n >> 1]
        A2 = A[n >> 1 :]
        cnt += BIT(A1)
        cnt += BIT(A2)
        i1, i2 = 0, 0
        for i in range(n):
            if i2 == len(A2):
                A[i] = A1[i1]
                i1 += 1
            elif i1 == len(A1):
                A[i] = A2[i2]
                i2 += 1
            elif A1[i1] <= A2[i2]:
                A[i] = A1[i1]
                i1 += 1
            else:
                A[i] = A2[i2]
                i2 += 1
                cnt += n // 2 - i1
    return cnt

a = [2, 15, 23, 32, 7, 19]
x = copy.copy(a)
ans = BIT(x)
print(ans)