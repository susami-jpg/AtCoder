from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import acosh, sqrt, factorial
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
    
H, W, h1, w1, h2, w2 = map(int, input().split())
A = [[0] * (W+1)] + [[0] + list(map(int, input().split())) for _ in range(H)]
h2 = min(h1, h2)
w2 = min(w1, w2)
acc_A = [[0] * (W+1) for _ in range(H+1)]

for i in range(1, H+1):
    for j in range(1, W+1):
        acc_A[i][j] = acc_A[i][j-1] + A[i][j]

for i in range(1, H+1):
    for j in range(1, W+1):
        acc_A[i][j] += acc_A[i-1][j]
    
#左上を(i, j)として、h*wのスタンプをおした時のscore
def get_score(i, j, h, w):
    r2 = min(H, i+h-1)
    c2 = min(W, j+w-1)
    return acc_A[r2][c2] - acc_A[r2][j-1] - acc_A[i-1][c2] + acc_A[i-1][j-1]

#B1は(i, j)を起点として横方向に幅w1のスライド最大値を記録する
B1 = [[0] * (W+1) for _ in range(H+1)]
for i in range(1, H+1):
    deq = maxQueue()
    for j in range(1, w1-w2+1):
        deq.push(get_score(i, j, h2, w2))
    for j in range(w1-w2+1, W+1):
        deq.push(get_score(i, j, h2, w2))
        B1[i][j-w1+w2] = deq.getMax()
        deq.remove()

#B2は(i, j)を起点として縦方向に幅h1のスライド最大値を記録する
B2 = [[0] * (W+1) for _ in range(H+1)]
for j in range(1, W+1):
    deq = maxQueue()
    for i in range(1, h1-h2+1):
        deq.push(B1[i][j])
    for i in range(h1-h2+1, H+1):
        deq.push(B1[i][j])
        B2[i-h1+h2][j] = deq.getMax()
        deq.remove()
ans = 0
for i in range(1, H+1):
    for j in range(1, W+1):
        prev_ans = ans
        if i+h1-1 <= H and j+w1-1 <= W:
            ans = max(ans, get_score(i, j, h1, w1) - B2[i][j])

print(ans)


        
        
    


    
