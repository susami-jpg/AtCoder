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

H, W = map(int, input().split())
A = [input() for _ in range(H)]
rec = [0] * 26
for i in range(H):
	for j in range(W):
		rec[ord(A[i][j])-97] += 1
	
def check(A, H, W):
	if H%2 == 0 and W%2 == 0:
		n4 = (H*W)//4
		for i in range(26):
			if A[i]%4:
				return False
		else:
			return True
	
	elif H%2 == 1 and W%2 == 1:
		n1 = 1
		n2 = (H-1)//2 + (W-1)//2
		n4 = (H-1)*(W-1)//4
		for i in range(26):
			if A[i] >= 4 and n4:
				if n4 - A[i]//4 >= 0:
					n4 -= A[i]//4
					A[i] %= 4
				else:
					A[i] -= n4*4
					n4 = 0
		for i in range(26):
			if A[i] >= 2 and n2:
				if n2 - A[i]//2 >= 0:
					n2 -= A[i]//2
					A[i] %= 2
				else:
					A[i] -= n2*2
					n2 = 0
		if sum(A) == 1 and n4 == 0 and n2 == 0:
			return True
		else:
			return False
	else:
		if H%2:
			H, W = W, H
		n2 = H//2
		n4 = H*(W-1)//4
		for i in range(26):
			if A[i] >= 4 and n4:
				if n4 - A[i]//4 >= 0:
					n4 -= A[i]//4
					A[i] %= 4
				else:
					A[i] -= n4*4
					n4 = 0
		for i in range(26):
			if A[i] >= 2 and n2:
				if n2 - A[i]//2 >= 0:
					n2 -= A[i]//2
					A[i] %= 2
				else:
					A[i] -= n2*2
					n2 = 0
		if n2 == 0 and n4 == 0:
			return True
		else:
			return False

if check(rec, H, W):
	print("Yes")
else:
	print("No")
	