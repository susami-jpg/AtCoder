from itertools import groupby

# RUN LENGTH ENCODING str -> list(tuple())
# example) "aabbbbaaca" -> [('a', 2), ('b', 4), ('a', 2), ('c', 1), ('a', 1)] 
def runLengthEncode(S: str) -> "list[tuple(str, int)]":
    grouped = groupby(S)
    res = []
    for k, v in grouped:
        res.append((k, int(len(list(v)))))
    return res

# RUN LENGTH DECODING list(tuple()) -> str
# example) [('a', 2), ('b', 4), ('a', 2), ('c', 1), ('a', 1)] -> "aabbbbaaca"
def runLengthDecode(L: "list[tuple]") -> str:
    res = ""
    for c, n in L:
        res += c * int(n)
    return res

# RUN LENGTH ENCODING str -> str
# example) "aabbbbaaca" -> "a2b4a2c1a1" 
def runLengthEncodeToString(S: str) -> str:
    grouped = groupby(S)
    res = ""
    for k, v in grouped:
        res += k + str(len(list(v)))
    return res

N, K = map(int, input().split())
S = input()
res = runLengthEncode(S)
n = len(res)
S = 0
r = 0
ans = 0
k = 0

for l in range(n):
    while r < n:
        if res[r][0] == '0':
            if k == K:
                break
            else:
                k += 1
        S += res[r][1]
        r += 1
    ans = max(ans, S)
    S -= res[l][1]
    if res[l][0] == '0':
        k -= 1

print(ans)
    
    
    