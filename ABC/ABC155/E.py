from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

#TLE
#桁数が大きいものをintで受け取るのはめっちゃ時間かかる
N = int(input())
S = [0] + list(map(int, list(str(N))))
L = len(S)
dp = [[INF] * 2 for _ in range(L)]
dp[0][0] = 0
dp[0][1] = 1

for i in range(1, L):
    for over in range(2):
        if over:
            dp[i][over] = min(dp[i-1][0]+S[i]+1, dp[i-1][1]+9-S[i])
        else:
            dp[i][over] = min(dp[i-1][0]+S[i], dp[i-1][1]+10-S[i])
print(dp[-1][0])

from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

S = [0] + list(map(int, list(input())))
L = len(S)
dp = [[0] * L for _ in range(2)]
dp[0][0] = 0
dp[1][0] = 1

for i in range(1, L):
    dp[1][i] = min(dp[0][i-1]+S[i]+1, dp[1][i-1]+9-S[i])
    dp[0][i] = min(dp[0][i-1]+S[i], dp[1][i-1]+10-S[i])
print(dp[0][-1])
