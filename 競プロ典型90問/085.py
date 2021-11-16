from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
INF = 10**15
MOD = 10**9+7
K = int(input())
ans = 0


#約数列挙
def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


div = make_divisors(K)
div.sort()
n = len(div)
for i in range(n):
    for j in range(i, n):
        a = div[i]
        b = div[j]
        if K%(a*b):continue
        c = K//(a*b)
        if c < b:continue
        ans += 1

print(ans)
