from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt, factorial
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

X, Y, A, B, C = map(int, input().split())
ans1 = -(-A//X) -(-B//X) -(-C//X)
ans2 = -(-A//Y) -(-B//Y) -(-C//Y)

if ans1 <= Y or ans2 <= X:
    print("Yes")
    exit()
    
def is_ok(lim, R1, R2, width):
    L = -(-R1//lim) - (-R2//lim)
    if L > width:
        return False
    else:
        return True
    
def meguru_bisect(ng, ok, R1, R2, width):
    '''
    初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
    まずis_okを定義すべし
    ng ok は  とり得る最小の値-1 とり得る最大の値+1
    最大最小が逆の場合はよしなにひっくり返す
    '''
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid, R1, R2, width):
            ok = mid
        else:
            ng = mid
    return ok

def check(R3, rest, width):
    if -(-R3//rest) <= width:
        return True
    else:
        return False
    
rectangle = [A, B, C]
for i in range(3):
    R3 = rectangle[i]
    R1 = rectangle[(i+1)%3]
    R2 = rectangle[(i+2)%3]
    lim = meguru_bisect(0, INF, R1, R2, X)
    #print(lim)
    if lim >= Y:continue
    if check(R3, Y-lim, X):
        print("Yes")
        exit()

for i in range(3):
    R3 = rectangle[i]
    R1 = rectangle[(i+1)%3]
    R2 = rectangle[(i+2)%3]
    lim = meguru_bisect(0, INF, R1, R2, Y)
    #print(lim)
    if lim >= X:continue
    if check(R3, X-lim, Y):
        print("Yes")
        exit()
print("No")
