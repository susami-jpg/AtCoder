# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 16:46:47 2021

@author: kazuk
"""

#math.floor/math.ceilの誤差を避ける
import math
x = 3
math.floor(x)
#-> x // 1

math.ceil(x)
#-> -(-x // 1)


# ２進数 -> 10進数への変換
def BinaryToDecimal(num):
    num = str(num)[::-1]
    decimal_number = 0
    for i in range(len(num)):
        decimal_number += int(num[i]) * (2 ** i)
    return decimal_number

n = 101001001111101011
ans = BinaryToDecimal(n)
print(ans)


# 10進数 -> 2進数への変換
def DeciamlToBinary(num):
    binary_number = ""
    while num > 0:
        binary_number += str(num % 2)
        num //= 2
    return int(binary_number[::-1])

n = 1234567890
ans = DeciamlToBinary(n)
print(ans)


#約数列挙
def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]



#複数の数字のリストを渡すとそれらの公約数を列挙したリストを返す
def check(num, i):
    for n in num:
        if n % i != 0:
            return False
    else:
        return True

#複数の数字をリストでもらいその共通する約数を列挙する
def make_divisors(num):
    lower_divisors , upper_divisors = [], []
    i = 1
    min_n = min(num)
    while i*i <= min_n:
        if check(num, i):
            lower_divisors.append(i)
        if i != min_n // i and check(num, min_n // i):
            upper_divisors.append(min_n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


# 桁の和を求める（intのまま計算するパターン）
def DigitSum(num):
    digit_sum = 0
    while num > 0:
        digit_sum += num % 10
        num //= 10
    return digit_sum

n = 1234567890
ans = DigitSum(n)
print(ans)


# 桁の和を求める（strに変更して計算するパターン）
def DigitSum(num):
    num = str(num)
    digit_sum = 0
    for i in range(len(num)):
        digit_sum += int(num[i])
    return digit_sum

n = 1234567890
ans = DigitSum(n)
print(ans)


#floatの誤差計算を防ぐためにintに変換して計算する
def FloatToInt(FLOAT):
    return int(FLOAT.replace(".", "")), len(FLOAT) - FLOAT.index(".") - 1 # tuple でreturn

n = "314.1592653589" # 開始はstrで渡す
x, y = FloatToInt(n)
print(x, y)



# 配列の累積和の部分和の最大値を求める
def MaxCumulativeSum(num_array, k): # 配列・区間幅
    max_cumulative_sum = [] # 区間幅分の部分和を格納する配列
    count = 0
    for i in range(k):
       count += num_array[i]
    max_cumulative_sum.append([count, 0, 0 + k]) # 部分和・左端・右端
    
    for i in range(len(num_array) - k):
        count += num_array[i + k]
        count -= num_array[i]
        max_cumulative_sum.append([count, i + 1, i + 1 + k])
    
    max_cumulative_sum.sort(key = lambda x: x[0], reverse = True) # 降順にソート
    return max_cumulative_sum[0] #リストで返す


a = [1, 4, -1, 9, 34, 21, -12, 31]
ans = MaxCumulativeSum(a, 3) # 配列・区間幅
print(ans)


#素数判定　あんまり早くない
def PrimaryCheck(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
            break
    return True


n = int(input())
num = PrimaryCheck(n)
print(num)


#エラトステネスの篩
#素数かどうかを0/1で判定した配列を返す
def primes(L):
    #Lは問題によって調節
    is_prime = [1] * L
    is_prime[0] = is_prime[1] = 0
    for i in range(2, L):
        if is_prime[i]:
            now = i+i
            while now < L:
                is_prime[now] = 0
                now += i
    return is_prime

#エラストテネスの篩
#具体的に素数を列挙
def primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]: continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]

n = 100
x = primes(n) # 素数の全列挙
l = len(x) # 素数の数
print(x)
print(l)



#区間篩
#a, bが与えられたときに区間[a, b]の間にある素数の数を数える
#b-aが小さいときに有効
#b未満の素数でない整数の最小の素因数はたかだか√b(それ以上大きい整数でbが割れないのは自明)
#なので、√b以下の素数の表をつくる
#√b以上の整数で区間[a, b]にある数字を割れる整数はない
#[2, √b]の表と[a, b]の表を別々に作っておいて
#[2, √b]の表から素数が得られるたびに素の素数の倍数を[a, b]から除けば[a, b]にある素数を列挙できる
#エラトステネスの区間篩：O(√a+(b-a)logloga)
#各整数の素因数分解：(b-a)loga)

from math import sqrt, ceil
#区間l, rは閉区間として扱う
def section_primes(l, r):
    sqrt_r = int(sqrt(r) + 1)
    dp1 = [1] * sqrt_r
    dp2 = [1] * (r-l+1)
    def change(n):
        return n-l
    dp1[0] = dp1[1] = 0
    for i in range(2, sqrt_r):
        if dp1[i] == 0:continue
        now = i+i
        while now < sqrt_r:
            dp1[now] = 0
            now += i
    if l == 0:
        dp2[0] = dp2[1] = 0
    if l == 1:
        dp2[0] = 0
    cnd = [i for i, c in enumerate(dp1) if c]
    for i in cnd:
        now = max(i+i, ceil(l/i) * i)
        while now < r+1:
            dp2[change(now)] = 0
            now += i
    return sum(dp2)



#０〜NまでのXORをとる
def XorToN(N: int) -> int:
    if N % 4 == 0:
        return N
    elif N % 4 == 1:
        return 1
    elif N % 4 == 2:
        return N + 1
    elif N % 4 == 3:
        return 0

x = XorToN(196)
print(x)





# nCk.pyよりも高速かな？（powを外に出した）
def combination(n, k):
    nCk = under = top = 1
    mod = 10 ** 9 + 7

    # 分母
    for i in range(2, k + 1):
        under *= i
        under %= mod

    # 分子
    for i in range(k):
        top *= (n - i)
        top %= mod

    nCk = top * pow(under, mod - 2, mod)

    return nCk % mod

n = combination(20, 10)
print(n)


#拡張ユークリッドの互除法
#ap + bq = d := gcd(a, b)となる (p, q, d) を返す
def extgcd(a: int, b: int) -> int:
    "ax + by = gcd(a,b) = d となる (x, y, d) を返す"
    if b == 0:
        return (1, 0, a)

    q, r = a // b, a % b
    x, y, d = extgcd(b, r)
    s, t = y, x - q * y

    return s, t, d # (qb + r)s + bt = dとなる s, t, d

ans = extgcd(30, 50)
print(ans)


#n進数
########関数部分##############
def Base_10_to_n(X, n):
    if X == 0:
        return '0'
    X_dumy = X
    out = ''
    while X_dumy>0:
        out = str(X_dumy%n)+out
        X_dumy = X_dumy//n
    return out
############################
"""
Xもnもint
戻り値はstr

#####関数をつかってみる．#####
######今回は二進数に変換######
x10 = 35
x2 = Base_10_to_n(x10, 2)
print( x2 )#"100011"が表示される．
"""

########関数部分##############
def Base_10_to_n_rec(X, n):
    if X//n:
        return Base_10_to_n_rec(X//n, n)+str(X%n)
    return str(X%n)
############################
 
"""
#####関数をつかってみる．#####
######今回は二進数に変換######
x10 = 35
x2 = Base_10_to_n(x10, 2)
print( x2 )#"100011"が表示される．
"""

########関数部分##############
def Base_n_to_10(X,n):
    out = 0
    for i in range(1,len(str(X))+1):
        out += int(X[-i])*(n**(i-1))
    return out#int out
############################
"""
Xはstr
nはint
戻り値はint

print(Base_n_to_10('253',4))#"55"と表示される．
"""


#上の関数ありき
#a進数nをb進数に変える
def Base_a_to_b(n, a, b):
    n = str(n)
    a = int(a)
    b = int(b)
    n10 = Base_n_to_10(n, a)
    nb = Base_10_to_n(n10, b)
    return nb



def change(N,shinsu):
    keta=0
    for i in range(10**9):
        if N<shinsu**i:
             keta+=i
             break
    ans=[0]*keta
    check=0
    for i in range(1,keta+1):
        j=N//(shinsu**(keta-i))
        ans[check]=j
        check+=1
        N-=(j)*(shinsu**(keta-i))
    return ans


#試し割法の素因数分解(1は空のリストを返すので注意)
#O(sqrt(N))
def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

"""
print(prime_factorize(1))
# []

print(prime_factorize(36))
# [2, 2, 3, 3]

print(prime_factorize(840))
# [2, 2, 2, 3, 5, 7]

素数とその個数を取得する場合
c = collections.Counter(prime_factorize(840))
print(c)
# Counter({2: 3, 3: 1, 5: 1, 7: 1})

これによって、NN の素因数分解において、aa の指数 (aa で何回割れるか) がわかります。ここでちょっとイヤなのは aa 自身が合成数である場合には、aa をさらに分解しなければならないように感じてしまうことです。しかしなんと、少しビックリするかもしれませんが

NN が aa で割れるとき、aa はかならず素数になっている
のです！！！！！！！なぜでしょう？？？
それは aa で試し割りする前に、aa を構成する各素因数 pp について NN が割れるだけ割られているからです。

たとえば N=60N=60 のとき、これは a=6a=6 で割り切れます。しかしその前の a=2a=2 の段階で、

60→30→15
60→30→15
という具合に、NN は 22 では割れない姿に変わり果てています。よって a=6a=6 の番が回ってきたときには、NN を割り切ることはできないのです。

まず、a≤N−−√a≤N まで割り終えたとき、NN がどうなっているかについて、以下の 2 つの場合が考えられます。

N=1N=1 になっている
N>1N>1 になっている
前者についてはもう素因数分解は完全に完了しています。それまでに得られた解を出力すればよいでしょう。

後者については、残った整数は素数です。なぜなら、それがもし合成数であれば、それを構成する素因数のうちの 1 つは N−−√N 以下になるはずだからです (N−−√N より大きい値を 2 回以上かけたら NN を超えることに注意)。
最後の NN には、もう、そんな小さな素因数は残っているはずがありません。
よって最後の NN は素数なので、それを答えに加えて終了します。
"""

#前計算なしのオイラー関数
#1,2,…,N のうち、N と互いに素であるものの個数
#N = 12なら1,5,7,11の4個
#上のprime_factrizeを使う
from collections import Counter
def Euler_count(n):
    fact = Counter(prime_factorize(n))
    cnt = n
    for key in fact.keys():
        cnt *= (1 - (1/key))
    return int(cnt)
    



"""nを素因数分解"""
"""2以上の整数n => [[素因数, 指数], ...]の2次元リスト"""

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

factorization(24) 

## [[2, 3], [3, 1]] 
##  24 = 2^3 * 3^1


#エラトステネスの篩を用いた高速素因数分解
#区間に使える
#recはdict型で区間内の任意の数字を素因数分解した結果をリストで得られる
#cntは素因数分解したときの素因数の個数(ex: 12 = 2*2*3よりcnt[12-l]は3)
from math import sqrt
from collections import defaultdict
def factorization(l, r):
    n = int(sqrt(r)) + 1
    
    #エラトステネスの篩
    #Lは問題によって調節
    L = 10**5+1
    is_prime = [1] * L
    is_prime[0] = is_prime[1] = 0
    for i in range(2, L):
        if is_prime[i]:
            now = i+i
            while now < L:
                is_prime[now] = 0
                now += i
                
    #valはnまでの素因数で割った結果を記録(val[i] != 1ならiは素数)
    val = [i for i in range(l, r+1)]
    #cntはその数を何回割ったかを記録
    cnt = [0] * (r-l+1)
    #区間内の数字についての素因数分解の結果を持つリスト
    rec = defaultdict(list)
    
    for i in range(n):
        if is_prime[i]:
            t = i
            c = 1
            while t ** c <= r:
                if l%(t**c) == 0:
                    k = l//(t**c)
                else:
                    k = l//(t**c) + 1
                #sはl以降の最初の(t**c)の倍数
                s = k*(t**c)
                while s <= r:
                    #s-lとすることで配列を0indexに戻す
                    cnt[s-l] += 1
                    #tのc条まで、すなわち素因数tでval[i]を割れるだけ割っておく
                    val[s-l] //= t
                    rec[s].append(t)
                    s += t**c
                #c(素因数の乗数)を増やす
                c += 1
    for i in range(l, r+1):
        #val[i-l]が素数の場合
        if val[i-l] != 1:
            cnt[i-l] += 1
            rec[i].append(val[i-l])
    #0はこのプログラムでは素数がたくさんカウントされるので戻す
    rec[0] = []
    cnt[0] = 0
    #cntを扱うときは欲しい値-lをすることを忘れずに
    #recは欲しい値そのままで大丈夫
    return cnt, rec
    
    


#SPFによる前処理とクエリの高速素数判定

#SmallestPrimeFactor
#自分の素因数の中で最小の素因数を記録
#前処理O(NloglogN)
#nは調べたい範囲の最大値
def SPF(n):
    spf = [i for i in range(n + 1)]
    check = [False] * (n + 1)
    spf[0] = 0
    spf[1] = 1
    check[0] = check[1] = True
    for i in range(2, int(n**0.5) + 1):
        if check[i]: continue
        for j in range(i, n + 1, i):
            if check[j]:continue
            spf[j] = i
            check[j] = True
    return spf


"""
primefactは素因数分解した結果を返す
ただしsetではない
ex: 9 -> 3, 3を返す
"""
#上のSPFによる前処理を終えた前提(関数内のspfは上の関数を使用した返り値のリストを参照している)
#クエリごとにO(logN)で素因数分解した結果を返す
#素因数分解なのでn=0,1はエラーを吐くので注意
def primefact(n, spf):
    fact = []
    while n != 1:
        fact.append(spf[n])
        n //= spf[n]
    return fact

#約数の個数
#関数SPFで前計算済み
#primefactでnの素因数分解の結果を用いてnの約数の個数を得る
from collections import Counter
def div_count(n, spf):
    fact = primefact(n, spf)
    rec = Counter(fact)
    cnt = 1
    for val in rec.values():
        cnt *= (val+1)
    return cnt


#高速約数列挙
#計算量は nn の約数の個数を σ(n)σ(n) として、O(σ(n))となります。n≤10**9 の範囲では、σ(n)≤1344σ(n)≤1344 (n=735134400 で最大) であることが知られていますので、十分高速です。
#関数SPFで前計算済み
#未ソートの約数列挙
from collections import Counter
def make_divisors(n, spf):
    pf = Counter(primefact(n, spf))
    res = [1]
    for p, e in pf.items():
        s = len(res)
        for i in range(s):
            v = 1
            for j in range(e):
                v *= p
                res.append(res[i]*v)
    #res.sort()
    return res
        

#オイラー関数
#関数SPFで前計算済み
#正の整数 N が与えられる。
#1,2,…,N のうち、N と互いに素であるものの個数
#N=pe11pe22…peKK
#N=p1e1p2e2…pKeK
#と素因数分解できるとき、オイラー関数値は

#φ(N)=N(1−1/p1)(1−1/p2)…(1−1/pK)
from collections import Counter
def Euler_count(n, spf):
    fact = primefact(n, spf)
    rec = Counter(fact)
    cnt = n
    for key in rec.keys():
        cnt *= (1 - (1/key))
    return cnt
        

#逆元によるnCkの高速計算
def inv(n): # MODを法とした逆元
    MOD = 10**9+7
    return pow(n, MOD-2, MOD)

MOD = 10**9+7
mx = 2*10**5
fact = [1] * (mx+1) # 階乗を格納するリスト
for i in range(mx):
    fact[i+1] = fact[i] * (i+1) % MOD # 階乗を計算
        
def comb(n, k):
    MOD = 10**9+7
    return (fact[n] * inv(fact[n-k]) * inv(fact[k])) % MOD # comb(n,k) = n!/((n-k)!k!)



# Euclidean Algorithm
def gcd(m, n):
    r = m % n
    return gcd(n, r) if r else n

def gcd_t(A):
    res = A[0]
    for i in range(1, len(A)):
        res = gcd(res, A[i])
    return res

# Euclidean Algorithm (non-recursive)
def gcd2(m, n):
    while n:
        m, n = n, m % n
    return m

# Extended Euclidean Algorithm
# a*x + b*y = c　となるようなa, bを返す
# c=gcd(a, b)とする
#gcd(a, b)でcが割り切れなければ整数解なし
def extgcd(a, b):
    if b:
        d, y, x = extgcd(b, a % b)
        y -= (a // b)*x
        return d, x, y
    return a, 1, 0

def extGCD(a,b):
    x, y, u, v = 1, 0, 0, 1
    while b:
        k = a // b
        x -= k * u
        y -= k * v
        x, u = u, x
        y, v = v, y
        a, b = b, a % b
    return x, y

# lcm (least common multiple)
def lcm(m, n):
    return m//gcd(m, n)*n

#5 3つ以上の数の最大公約数を計算する
def gcd_t(list_g1):
    for i in reversed(range(1, min(list_g1)+1)):
        for j in list_g1:
            if j%i!=0:
                break
        else:
            return i

#10 最大の数の倍数から最小公倍数を計算
def lcm(list_l):
    greatest = max(list_l)
    i = 1
    while True:
        for j in list_l:
            if (greatest * i) % j != 0:
                i += 1
                break
        else:
            return greatest * i


#ここからlcm_2まででリスト内の複数の数字の最小公倍数を返す関数
from math import gcd

# 2数を受け取って最小公倍数を返す関数
def lcm(a, b):
    y = a*b // gcd(a, b)
    return int(y)

# 可変引数を受け取って最小公倍数を返す関数
import functools

def lcm_2(*vals):
    return functools.reduce(lcm, vals)


#複素数関連
import math, cmath
#complex型は複素数を表す　実部、虚部の順
vector = complex(5, 3)

#長さが1で偏角が2πNの複素数をrとすると、答えはp=(p0−o)r+oです。
#cmath.polar(x) xの極座標表現を返します。
#cmath.rect(r, phi) 極座標 r, phi を持つ複素数 x を返します。
n = int(input())
r = cmath.rect(1, 2*math.pi/n)
ans = complex(3, 3) + vector * r
#ans.real:= 実部、ans.imag:= 虚部
print(ans.real, ans.imag)


def gcd(x, y):
    if x == 0:return y
    else:
        return gcd(y%x, x)

#aが分子でbが分母の有理数を約分して返す
#分母bが0ならa=1、b=0として返す
#a=0の場合は考慮していないので注意
#bは正に変換する
def rational_nun(a, b):
    if b == 0:
        return (1, 0)
    if b < 0:
        a *= -1
        b *= -1
    g = gcd(abs(a), b)
    a //= g
    b //= g
    return (a, b)

#二つの有理数の大小を比較してその大小を返す
#r1、r2は(a, b)の形で渡す(aは分子、bは分母)
#r1 > r2なら1を返す
#r1 == r2なら0を返す
#r1 < r2なら-1を返す
def compare(r1, r2):
    res = r1[0]*r2[1] - r2[0]*r1[1]
    if res > 0:
        return 1
    elif res == 0:
        return 0
    else:
        return -1
    
def popcount(x):
    '''xの立っているビット数をカウントする関数
    (xは64bit整数)'''

    # 2bitごとの組に分け、立っているビット数を2bitで表現する
    x = x - ((x >> 1) & 0x5555555555555555)

    # 4bit整数に 上位2bit + 下位2bit を計算した値を入れる
    x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)

    x = (x + (x >> 4)) & 0x0f0f0f0f0f0f0f0f # 8bitごと
    x = x + (x >> 8) # 16bitごと
    x = x + (x >> 16) # 32bitごと
    x = x + (x >> 32) # 64bitごと = 全部の合計
    return x & 0x0000007f