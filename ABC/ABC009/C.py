from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

N, K = map(int, input().split())
S = list(input())

char_set = sorted(S)

def is_ok(fix, rest, ban):
    n = len(fix)
    diff = 0
    for i in range(n):
        if S[i] != fix[i]:
            diff += 1
    
    if diff > K:
        return False
    
    chr_cnt_S = [0] * 26
    chr_cnt_rest = [0] * 26

    for i in range(n, N):
        chr_cnt_S[ord(S[i])-97] += 1
        
    for i, c in enumerate(rest):
        if i == ban:continue
        chr_cnt_rest[ord(c)-97] += 1
    
    #print(chr_cnt_S)
    #print(chr_cnt_rest)
    #print(diff)
    
    d = 0
    for i in range(26):
        d += abs(chr_cnt_S[i] - chr_cnt_rest[i])
    d //= 2
    diff += d
    if diff > K:
        return False
    else:
        return True

T = ""
L = 0
R = len(char_set)
while L < N:
    #print(T)
    for i in range(R):
        if is_ok(T+char_set[i], char_set, i):
            T += char_set[i]
            char_set.pop(i)
            L += 1
            R -= 1
            break
print(T)
