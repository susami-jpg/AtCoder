from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
INF = 10**15
MOD = 10**9+7

import heapq
from sys import exit
from bisect import bisect_left, bisect_right, insort_left

class HeapDict:
    def __init__(self):
        self.h=[]
        self.d=dict()
    
    def get(self,x):
        if len(self.h) <= x:
            return False
        else:
            return self.h[x]
    
    def add_element(self, x):
        self.h.append(x)
        if x not in self.d:
            self.d[x]=1
        else:
            self.d[x]+=1
    
    def set_sort(self):
        self.h.sort()
    
    def set_rsort(self):
        self.h.sort(reverse=True)

    def insert(self,x):
        insort_left(self.h,x)
        if x not in self.d:
            self.d[x]=1
        else:
            self.d[x]+=1

    def erase(self,x):
        if x not in self.d or self.d[x]==0:
            print(x,'is not in HeapDict')
            exit()
        else:
            self.d[x]-=1
            ind = bisect_left(self.h, x)
            self.h.pop(ind)

    def is_exist(self,x):
        if x in self.d and self.d[x]!=0:
            return True
        else:
            return False

    def get_min(self):
        return self.h[0]

    def get_max(self):
        return self.h[-1]

    #HeapDictの中身がなければTrue
    def empty(self):
        if len(self.h) == 0:
            return True
        else:
            return False

    def LessThan(self, K: int) -> int:
        '配列Aの中のうち、k未満の個数と終わりの0indexを返すライブラリ'
        '-1の時は解が無い時'
        ans = bisect_left(self.h, K)
        return ans, (-1 if ans == 0 else ans - 1)

    def OrLessThan(self, K: int) -> int:
        '配列Aの中のうち、k以下の個数と終わりの0indexを返すライブラリ'
        '-1の時は解が無い時'
        ans = bisect_right(self.h, K)
        return ans, (-1 if ans == 0 else ans - 1)

    def More(self, K: int) -> int:
        '配列Aの中のうち、kより大きいものの個数と始まりの0indexを返すライブラリ'
        '-1の時は解が無い時'
        ans = bisect_right(self.h, K)
        l = len(self.h)
        return l - ans, (ans if ans <= l - 1 else -1)

    def OrMore(self, K: int) -> int:
        '配列Aの中のうち、k以上の個数と始まりの0indexを返すライブラリ'
        '-1の時は解が無い時'
        ans = bisect_left(self.h, K)
        l = len(self.h)
        return l - ans, (ans if ans <= l - 1 else -1)

#dict型なら複数のHeapDictの集合を扱える
#'key' in dictでkeyの存在を確認できる
input = stdin.readline
H = [HeapDict() for _ in range(26)]
N = int(input())
S = list(input())
for i in range(N):
    H[ord(S[i])-97].add_element(i)

for i in range(26):
    H[i].set_sort()

Q = int(input())

for _ in range(Q):
    q, l, r = input().split()
    if q == "1":
        l = int(l) - 1
        now = S[l]
        H[ord(now)-97].erase(l)
        S[l] = r
        H[ord(r)-97].insert(l)
    else:
        l = int(l) - 1
        r = int(r)
        ans = 0
        for c in range(26):
            _, ind = H[c].OrMore(l)
            if ind != -1 and H[c].get(ind) < r:
                ans += 1
        print(ans)
