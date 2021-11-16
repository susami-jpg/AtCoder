from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

S1 = list(input())
S2 = list(input())
S3 = list(input())

str_set = list(set(list(S1 + S2 + S3)))

if len(str_set) > 10:
    print('UNSOLVABLE')
    exit()
    
N = len(str_set)

def check(S, str_dict):
    if str_dict[S[0]] == 0:
        return False
    else:
        return True

def str_to_int(S, str_dict):
    res = 0
    for s in S:
        res *= 10
        res += str_dict[s]
    return res

for perm in permutations(range(10), N):
    str_dict = dict()
    for s, n in zip(str_set, perm):
        str_dict[s] = n
    ok = True
    for Si in [S1, S2, S3]:
        if not check(Si, str_dict):
            ok = False
    
        
    if ok:
        N1 = str_to_int(S1, str_dict)
        N2 = str_to_int(S2, str_dict)
        N3 = str_to_int(S3, str_dict)
        
        if N1 + N2 == N3:
            for i in [N1, N2, N3]:
                print(i)
            exit()
else:
    print('UNSOLVABLE')
    