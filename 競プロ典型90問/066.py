from collections import defaultdict

N = int(input())
array = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for i in range(N-1):
    for j in range(i+1, N):
        Li, Ri = array[i]
        Lj, Rj = array[j]
        cnd = (Ri-Li+1) * (Rj-Lj+1)
        cnt = 0
        for now in range(Li, Ri+1):
            if Rj >= now:
                cnt += max(0, now-Lj)
            else:
                cnt += (Rj-Lj+1)
        ans += cnt/cnd
print(ans)



