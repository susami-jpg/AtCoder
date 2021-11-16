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

def multi_input():
    while True:
        try:
            yield input()
        except EOFError:
            break

def step1():
    query = list(multi_input())
    #print(query)
    Q = len(query)
    i = 0
    M = int(query[i])
    
    #料理情報取得
    stock = defaultdict(int)
    price = dict()
    for _ in range(M):
        i += 1
        d, s, p = map(int, query[i].split())
        stock[d] = s
        price[d] = p
    
    for j in range(i+1, Q):
        _, T, D, N = query[j].split()
        T = int(T)
        D = int(D)
        N = int(N)
        if stock[D] >= N:
            for _ in range(N):
                print("received order", T, D)
            stock[D] -= N
        else:
            print("sold out", T)

def step2():
    query = list(multi_input())
    Q = len(query)
    #print(query)
    i = 0
    M, K = map(int, query[i].split())
    
    #料理情報取得
    stock = defaultdict(int)
    price = dict()
    for _ in range(M):
        i += 1
        d, s, p = map(int, query[i].split())
        stock[d] = s
        price[d] = p
    
    #調理順の管理
    waiting = []
    using_woven = 0
    cooking = defaultdict(int)

    for j in range(i+1, Q):
        info = list(query[j].split())
        #print(info)
        #注文情報
        if len(info) == 4 and info[0] == "received" and info[1] == "order":
            T, D = int(info[2]), int(info[3])
            if using_woven < K:
                print(D)
                using_woven += 1
                cooking[D] += 1
            else:
                print("wait")
                heappush(waiting, (j, D))
        #完成情報
        elif len(info) == 2 and info[0] == "complete":
            D = int(info[1])
            if cooking[D]:
                cooking[D] -= 1
                if waiting:
                    _, nxt = heappop(waiting)
                    print("ok", nxt)
                    cooking[nxt] += 1
                else:
                    print("ok")
                    using_woven -= 1
            else:
                print("unexpected input")
        else:
            print("unexpected input")

def step3():
    query = list(multi_input())
    Q = len(query)
    #print(query)
    i = 0
    M = int(query[i])
    #料理情報取得
    stock = defaultdict(int)
    price = dict()
    for _ in range(M):
        i += 1
        d, s, p = map(int, query[i].split())
        stock[d] = s
        price[d] = p
    
    #調理順の管理
    waiting = []
    using_woven = 0
    cooking = defaultdict(int)
    delivery = defaultdict(list)
    for j in range(i+1, Q):
        info = list(query[j].split())
        #print(info)
        
        #注文情報
        if len(info) == 4 and info[0] == "received" and info[1] == "order":
            T, D = int(info[2]), int(info[3])
            heappush(delivery[D], (j, T))
            
        #完成情報
        elif len(info) == 2 and info[0] == "complete":
            D = int(info[1])
            if delivery[D]:
                _, T = heappop(delivery[D])
                print("ready", T, D)
        else:
            print("unexpected input")
            
def step4():
    query = list(multi_input())
    Q = len(query)
    #print(query)
    i = 0
    M = int(query[i])
    #料理情報取得
    stock = defaultdict(int)
    price = dict()
    for _ in range(M):
        i += 1
        d, s, p = map(int, query[i].split())
        stock[d] = s
        price[d] = p
    
    #席ごとの情報管理
    sum_price = defaultdict(int)
    is_delivered = defaultdict(int)
    orderd_cnt = defaultdict(int)
        
    for j in range(i+1, Q):
        info = list(query[j].split())
        #print(info)
        
        #注文受理情報
        if len(info) == 4 and info[0] == "received" and info[1] == "order":
            T, D = int(info[2]), int(info[3])
            orderd_cnt[T] += 1
            sum_price[T] += price[D]
            is_delivered[(T, D)] += 1
            
        #注文提供情報
        elif len(info) == 3 and info[0] == "ready":
            T, D = int(info[1]), int(info[2])
            if is_delivered[(T, D)] >= 1:
                is_delivered[(T, D)] -= 1
                orderd_cnt[T] -= 1

        #会計申請情報
        elif len(info) == 2 and info[0] == "check":
            T = int(info[1])
            if orderd_cnt[T] == 0:
                print(sum_price[T])
                sum_price[T] = 0
            else:
                print("please wait")
    
        
    
    

s = int(input())
if s == 1:
    step1()
elif s == 2:
    step2()
elif s == 3:
    step3()
else:
    step4()