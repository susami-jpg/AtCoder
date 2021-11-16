# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 00:39:35 2021

@author: kazuk
"""

import heapq
from sys import exit
from bisect import bisect_left, bisect_right, insort_left

#C++のmultisetに近い
class HeapDict:
    def __init__(self):
        self.h=[]
        self.d=dict()

    def insert(self,x):
        insort_left(self.h,x)
        if x not in self.d:
            self.d[x]=1
        else:
            self.d[x]+=1

    def erase(self,x):
        if x not in self.d or self.d[x]==0:
            print(x,"is not in HeapDict")
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
        
    def get_list(self):
        return self.h
    
    def More(self, x) -> int:
        '配列Aの中のうち、xより大きいものの個数と始まりの0indexを返すライブラリ'
        '-1の時は解が無い時'
        ans = bisect_right(self.h, x)
        l = len(self.h)
        return l - ans, (ans if ans <= l - 1 else -1)
    
    def LessThan(self, x) -> int:
        '配列Aの中のうち、x未満の個数と終わりの0indexを返すライブラリ'
        '-1の時は解が無い時'
        ans = bisect_left(self.h, x)
        return ans, (-1 if ans == 0 else ans - 1)

#dict型なら複数のHeapDictの集合を扱える
#'key' in dictでkeyの存在を確認できる
H = dict()
H[0] = HeapDict()




"""
〇O(logn)で要素の挿入
〇O(logn)で要素の削除
〇O(1)で要素の存在確認
〇O(1)で最小値の取得

これは単純にheapqの上位互換です。
C++のmultisetやsetとかなり似ています。
二分探索ができないだけです。
"""

import heapq
from sys import exit
class HeapDict:
    def __init__(self):
        self.h=[]
        self.d=dict()

    def insert(self,x):
        heapq.heappush(self.h,x)
        if x not in self.d:
            self.d[x]=1
        else:
            self.d[x]+=1

    def erase(self,x):
        if x not in self.d or self.d[x]==0:
            print(x,"is not in HeapDict")
            exit()
        else:
            self.d[x]-=1

        while len(self.h)!=0:
            if self.d[self.h[0]]==0:
                heapq.heappop(self.h)
            else:
                break

    def is_exist(self,x):
        if x in self.d and self.d[x]!=0:
            return True
        else:
            return False

    def get_min(self):
        return self.h[0]
    
    #HeapDictの中身がなければTrue
    def empty(self):
        if len(self.h) == 0:
            return True
        else:
            return False
    



