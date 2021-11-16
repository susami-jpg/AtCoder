from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

#複素数関連
import math, cmath
N = int(input())
x0, y0 = map(int, input().split())
xh, yh = map(int, input().split())

#complex型は複素数を表す　実部、虚部の順
vector = complex((xh+x0)/2, (yh+y0)/2)

#長さが1で偏角が2πNの複素数をrとすると、答えはp=(p0−o)r+oです。
#cmath.polar(x) xの極座標表現を返します。
#cmath.rect(r, phi) 極座標 r, phi を持つ複素数 x を返します。
r = cmath.rect(1, 2*math.pi/N)
ans = vector + complex(x0-vector.real, y0-vector.imag) * r
#ans.real:= 実部、ans.imag:= 虚部
print(ans.real, ans.imag)
