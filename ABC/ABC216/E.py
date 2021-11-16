from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right
from math import sqrt
INF = 10**15
MOD = 10**9+7

N, K = map(int, input().split())
A = list(map(int, input().split()))

def S(a, l, n):
    return (a+l)*n//2

ans = 0
if sum(A) <= K:
    for a in A:
        ans += S(1, a, a)
    print(ans)
    exit()

#得る満足度の最小値をx以上にできるか?
def is_ok(x):
    cnt = 0
    for a in A:
        if a-x > 0:
            cnt += a-x
    if cnt > K:
        return False
    else:
        return True

def meguru_bisect(ng, ok):
    while abs(ng-ok) > 1:
        mid = (ng+ok)//2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

lim = meguru_bisect(0, 10**10)
cnt = 0
ans = 0
for a in A:
    if a-lim > 0:
        cnt += a-lim
        #初項はlim+1になることに注意
        ans += S(lim+1, a, a-lim)

#lim自体はいくつ獲れるか?
#rest個は絶対ある(もしなければlim=x-1になるはず)
rest = K-cnt
ans += lim * rest
print(ans)





