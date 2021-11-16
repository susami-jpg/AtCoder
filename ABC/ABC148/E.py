from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt, ceil
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

N = int(input())
if N%2:
    print(0)
else:
    ans = 0
    for i in range(30):
        p = 10 * pow(5, i)
        ans += N//p
    print(ans)
"""   
def f(n):
    if n < 2:
        return 1
    else:
        return n*f(n-2)
c = str(f(N))[::-1]
cnt = 0
i = 0
while 1:
    if c[i] == "0":
        cnt += 1
        i += 1
    else:
        print(cnt)
        break

"""