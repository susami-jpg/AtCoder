# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 22:54:38 2021

@author: kazuk
"""


import heapq
class Heapq:
    def __init__(self, arr, desc=False):
        if desc:
            arr = [-a for a in arr]
        self.sign = -1 if desc else 1
        self.hq = arr
        heapq.heapify(self.hq)
 
    def pop(self):
        return heapq.heappop(self.hq) * self.sign
 
    def push(self, a):
        heapq.heappush(self.hq, a * self.sign)
 
    def top(self):
        return self.hq[0] * self.sign


"""
初期化
q = Heapq(arr, desc) のように書けばいいです

第1引数 arr は初期化に使う配列です 空っぽから始める場合は []でいいです
第2引数 desc は大きい順に取り出すなら True、小さい順ならFalse です。Falseは省略可です。
pop()
q.pop() のようにすると値が返ります
一番小さいの or 一番大きいのを集合から取り出します。
初期化時 desc=Trueを指定していたなら大きい方が出てきます。
取り出された要素は集合から消えます。

push()
q.push(a) のようにすると集合に aを追加します

top()
q.top() のようにすると値が返ります
一番小さいの or 一番大きいのを参照できます
初期化時 desc=Trueを指定していたなら大きい方が出てきます。
pop()に似てますが、参照するだけで、集合から値が消えることはありません。
O(1)でめっちゃ速いです
"""