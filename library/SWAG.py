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

class maxStack():
    def __init__(self):
        #aはスライドさせていく中で実際に入れる次の値
        self.a = []
        #mxは暫定のmaxの値をstackで管理
        self.mx = []
    
    def getMax(self):
        if len(self.mx):
            return self.mx[-1]
        else:
            #ここは適宜変更
            return 0
        
    def remove(self):
        self.a.pop()
        self.mx.pop()
    
    def push(self, x):
        self.a.append(x)
        self.mx.append(max(x, self.getMax()))
    
    def size(self):
        return len(self.a)
    
    def top(self):
        if len(self.a):
            return self.a[-1]

class maxQueue():
    def __init__(self):
        #sはpop専用のstack、上述のmaxStackを使う
        self.s = maxStack()
        #tはpush専用のstack、上述のmaxStackを使う
        self.t = maxStack()
    
    def mv(self):
        #ここで移し替えるときにsではtのmxの値が逆順に入るのではなく、
        #tのaの値がpopされる順にあらたにmxが更新されていく
        while self.t.size():
            self.s.push(self.t.top())
            self.t.remove()

    def push(self, x):
        self.t.push(x)
    
    def remove(self):
        if self.s.size() == 0:
            self.mv()
        self.s.remove()
    
    def getMax(self):
        return max(self.t.getMax(), self.s.getMax())
    

#配列Aと任意の長さwidthをもらい、len(A)-width+1の長さの配列Bを返す
#B[i]:= 0indexedで[i:i+width)のなかの最大値
def rangeMax(A, width):
    a = A + [0]
    print(len(a))
    B = [0] * (len(a)-width)
    que = maxQueue()
    for i in range(len(a)):
        if i-width >= 0:
            B[i-width] = que.getMax()
            que.remove()
        que.push(a[i])
    return B

A = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 2, 9, 1, 3, 4, 5]
            
    
        
class minStack():
    def __init__(self):
        #aはスライドさせていく中で実際に入れる次の値
        self.a = []
        #mxは暫定のmaxの値をstackで管理
        self.mx = []
    
    def getMin(self):
        if len(self.mx):
            return self.mx[-1]
        else:
            #ここは適宜変更
            return INF
        
    def remove(self):
        self.a.pop()
        self.mx.pop()
    
    def push(self, x):
        self.a.append(x)
        self.mx.append(min(x, self.getMin()))
    
    def size(self):
        return len(self.a)
    
    def top(self):
        if len(self.a):
            return self.a[-1]

class minQueue():
    def __init__(self):
        #sはpop専用のstack、上述のmaxStackを使う
        self.s = minStack()
        #tはpush専用のstack、上述のmaxStackを使う
        self.t = minStack()
    
    def mv(self):
        #ここで移し替えるときにsではtのmxの値が逆順に入るのではなく、
        #tのaの値がpopされる順にあらたにmxが更新されていく
        while self.t.size():
            self.s.push(self.t.top())
            self.t.remove()

    def push(self, x):
        self.t.push(x)
    
    def remove(self):
        if self.s.size() == 0:
            self.mv()
        self.s.remove()
    
    def push(self, x):
        self.t.push(x)
    
    def getMin(self):
        return min(self.t.getMin(), self.s.getMin())
    

#配列Aと任意の長さwidthをもらい、len(A)-width+1の長さの配列Bを返す
#B[i]:= 0indexedで[i:i+width)のなかの最大値
def rangeMin(A, width):
    a = A + [0]
    print(a)
    B = [0] * (len(a)-width)
    que = minQueue()
    for i in range(len(a)):
        if i-width >= 0:
            B[i-width] = que.getMin()
            que.remove()
        que.push(a[i])
    return B

print(*rangeMax(A, 3))
print(*rangeMin(A, 3))
