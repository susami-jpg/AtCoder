
"""
def main():
    from sys import exit, stdin, setrecursionlimit
    from bisect import bisect_left, bisect_right, insort_left, insort_right
    from collections import defaultdict, deque
    from heapq import heappop, heappush, heapify
    from itertools import permutations, combinations, accumulate
    from math import sqrt
    INF = 10**15
    MOD = 10**9+7

    input = stdin.readline
    L, Q = map(int, input().split())
    from array import array
    # <= #10**9
    wood = array('i', [0, L])
    
    ans = []
    def LessThan(K: int, A: list) -> int:
        '配列Aの中のうち、k未満の個数と終わりの0indexを返すライブラリ'
        '-1の時は解が無い時'
        ans = bisect_left(A, K)
        return ans, (-1 if ans == 0 else ans - 1)
    
    for _ in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            wood.insert(bisect_left(wood, x), x)
        else:
            _, l = LessThan(x, wood)
            left = wood[l]
            right = wood[l+1]
            ans.append(right-left)
    for a in ans:
        print(a)

if __name__ == "__main__":
    main()
"""

"""
整数値を取る平衡二分木を作る
取りうる整数値 x の範囲を 1≤x<L とするとき、構築は O(1) 、挿入・削除・検索は O(log⁡L) でできる
なお本稿では簡単のため、同じ値を複数個追加することはない（すでに存在する値を追加しようとした場合は何も起きない）としています。
-> setと同じで順序維持
"""

#C++のsetに近い
class BinaryTrie:
    def __init__(self, max_query=2*10**5, bitlen=30):
        n = max_query * bitlen
        self.nodes = [-1] * (2 * n)
        self.cnt = [0] * n
        self.id = 0
        self.bitlen = bitlen
 
    # xの挿入
    def insert(self,x):
        pt = 0
        for i in range(self.bitlen-1,-1,-1):
            y = x>>i&1
            if self.nodes[2*pt+y] == -1:
                self.id += 1
                self.nodes[2*pt+y] = self.id
            self.cnt[pt] += 1
            pt = self.nodes[2*pt+y]
        self.cnt[pt] += 1
 
    # 昇順x番目の値
    def kth_elm(self,x):
        pt, ans = 0, 0
        for i in range(self.bitlen-1,-1,-1):
            ans <<= 1
            if self.nodes[2*pt] != -1 and self.cnt[self.nodes[2*pt]] > 0:
                if self.cnt[self.nodes[2*pt]] >= x:
                    pt = self.nodes[2*pt]
                else:
                    x -= self.cnt[self.nodes[2*pt]]
                    pt = self.nodes[2*pt+1]
                    ans += 1
            else:
                pt = self.nodes[2*pt+1]
                ans += 1
        return ans

    # x以上の最小要素が昇順何番目か
    def lower_bound(self,x):
        pt, ans = 0, 1
        for i in range(self.bitlen-1,-1,-1):
            if pt == -1: break
            if x>>i&1 and self.nodes[2*pt] != -1:
                ans += self.cnt[self.nodes[2*pt]]
            pt = self.nodes[2*pt+(x>>i&1)]
        return ans


L, Q = map(int, input().split())
BIT = BinaryTrie()
BIT.insert(0)
BIT.insert(L)
for _ in range(Q):
    c, x = map(int, input().split())
    if c == 1:
        BIT.insert(x)
    else:
        r = BIT.lower_bound(x)
        print(BIT.kth_elm(r) - BIT.kth_elm(r-1))
        
        
    
