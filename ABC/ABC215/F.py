from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]
points.sort()

def is_ok(d):
    max_y = -INF
    min_y = INF
    deq = deque()
    #ok_y = False
    for x, y in points:
        while deq and deq[0][0] <= x-d:
            ok_y = True
            cur_y = deq[0][1]
            max_y = max(max_y, cur_y)
            min_y = min(min_y, cur_y)
            deq.popleft()
        #if ok_y and (abs(max_y - y) >= d or abs(y - min_y) >= d):
        if max_y - y >= d or y - min_y >= d:
            return True
        deq.append((x, y))
    else:
        return False
                


def meguru_bisect(ng, ok):
    '''
    初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
    まずis_okを定義すべし
    ng ok は  とり得る最小の値-1 とり得る最大の値+1
    最大最小が逆の場合はよしなにひっくり返す
    '''
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

ans = meguru_bisect(10**10, 0)
print(ans)


#TLE
#原因不明
def main():
    from sys import exit, stdin, setrecursionlimit
    from bisect import bisect_left, bisect_right, insort_left, insort_right
    from collections import defaultdict, deque
    from heapq import heappop, heappush, heapify
    from itertools import permutations, combinations, accumulate
    from math import sqrt
    from copy import copy, deepcopy
    INF = 10**15
    MOD = 10**9+7

    input = stdin.readline

    N = int(input())
    points = [tuple(map(int, input().split())) for _ in range(N)]
    points.sort()
    X = [x for x, _ in points]

    def OrLessThan(K: int, A: list) -> int:
        '配列Aの中のうち、k以下の個数と終わりの0indexを返すライブラリ'
        '-1の時は解が無い時'
        ans = bisect_right(A, K)
        return ans, (-1 if ans == 0 else ans - 1)

    def is_ok(d):
        ok_y = False
        max_y = -INF
        min_y = INF
        prev = -1
        for i in range(N):
            xi, yi = points[i]
            c, ind = OrLessThan(xi-d, X)
            if c == 0:continue
            for j in range(prev+1, ind+1):
                xj, yj = points[j]
                if xi - xj >= d:
                    max_y = max(max_y, yj)
                    min_y = min(min_y, yj)
                    prev = j
                    ok_y = True
            
            if ok_y:
                if abs(yi-max_y) >= d or abs(yi-min_y) >= d:
                    return True
        else:
            return False
                    


    def meguru_bisect(ng, ok):
        '''
        初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
        まずis_okを定義すべし
        ng ok は  とり得る最小の値-1 とり得る最大の値+1
        最大最小が逆の場合はよしなにひっくり返す
        '''
        while (abs(ok - ng) > 1):
            mid = (ok + ng) // 2
            if is_ok(mid):
                ok = mid
            else:
                ng = mid
        return ok

    ans = meguru_bisect(10**10, 0)
    print(ans)

if __name__ == '__main__':
    main()

