# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 16:38:34 2021

@author: kazuk
"""

# 計算量は O (NlogN)
#狭義単調増加部分列
from bisect import bisect_left

def LIS(A, N): # 配列・長さ
    INF = 10 ** 18
    dp = [INF] * n
    for i in A:
        x = bisect_left(dp, i)
        dp[x] = i
    return(bisect_left(dp, INF))

n = 5
a = [5, 1, 3, 2, 4]
ans = LIS(a, n)
print(ans)


#広義単調増加部分列
def improper_LIS(L):
    from bisect import bisect
    seq = []
    for ai in L:
        pos = bisect(seq, ai)
        if len(seq) <= pos:
            seq.append(ai)
        else:
            seq[pos] = ai
    return len(seq)