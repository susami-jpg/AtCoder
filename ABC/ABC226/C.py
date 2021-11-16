from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt, factorial
from decimal import Decimal
#decimalには文字列で渡す PyPyは遅いのでPython3で提出する
#d1 = Decimal('1.1') d2 = Decimal('2.3') -> d1 + d2などの演算で浮動小数点数での誤差がなくなる(割り算もok)
INF = 10**15
MOD = 10**9+7

N = int(input())
edge = []
cost = [-1] * N
nes = defaultdict(list)

for i in range(N):
    inp = list(map(int, input().split()))
    if len(inp) <= 2:
        T, K = inp[0], inp[1]
        cost[i] = T
    else:
        T, K, A = inp[0], inp[1], inp[2:]
        cost[i] = T
        nes[i] = A
ans = cost[N-1]
nes_now = nes[N-1]
used = [0] * N
while 1:
    nxt_nes = set()
    prev_ans = ans
    for a in nes_now:
        if used[a]:continue
        ans += cost[a-1]
        used[a] = 1
        nxt_nes |= set(nes[a-1])
    if prev_ans == ans:
        break
    nes_now = nxt_nes
print(ans)

        
    
    
        

