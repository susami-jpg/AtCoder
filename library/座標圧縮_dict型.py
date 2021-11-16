# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 19:03:11 2021

@author: kazuk
"""

def CC(A: list) -> list:
    "座標圧縮"
    B = {i: j for i, j in enumerate(sorted(A))}
    return B

x = [2, 5, 1, 21, 312, 23, 21]
ans = CC(x)
print(ans)

"""
{1: 1, 2: 2, 5: 3, 21: 4, 23: 5, 312: 6}
"""

def CC_2D(A: list) -> list:
    X = set()
    Y = set()
    for x, y in A:
        X.add(x)
        X.add(x+1)
        Y.add(y)
        Y.add(y)
        
    X = {i: j for i, j in enumerate(sorted(list(X)))}
    Y = {i: j for i, j in enumerate(sorted(list(Y)))}
    return X, Y

#defaultdictの初期値の変更
defaultdict(lambda: -1)

#辞書に初期値がない場合は、デフォルト値で初期化する
#defaultdictでできたのは辞書型ではなくタプルindex[0]がキーでindex[1]がvalue
from collections import defaultdict
data = defaultdict(int)
data['a'] += 1
data
#defaultdict(<class 'int'>, {'a': 1})
data['a'] += 1
#defaultdict(<class 'int'>, {'a': 2})
data[("y","x")] += 1
#こんなのもいける
#defaultdictはdictに変換しないと中身を取り出せないが、あるキーがあるかどうかはそのままでok


#辞書オブジェクトに対してinを使うとキーの存在確認になる。存在しないことの確認にはnot inを使う。
d = {'key1': 'val1', 'key2': 'val2', 'key3': 'val3'}

print('key1' in d)
# True

print('val1' in d)
# False

print('key4' not in d)
# True


#辞書の値（value）の存在を確認、取得（検索）: in演算子, values()
print('val1' in d.values())
# True

print('val4' not in d.values())
# True


#defaultdict => dict 
d = defaultdict(lambda: defaultdict(int))
d['key']['a'] += 3

print(type(d))

d = dict(d)
print(type(d))


#Pythonの辞書（dict）のforループ処理（keys, values, items）
#keys(): 各要素のキーkeyに対してforループ処理 辞書オブジェクトをそのままfor文で回すとキーkeyが取得できる。
for k in d.keys():
    print(k)
#values(): 各要素の値valueに対してforループ処理
for v in d.values():
    print(v)
#items(): 各要素のキーkeyと値valueに対してforループ処理
for k, v in d.items():
    print(k, v)
    

#key昇順ソート
dct = { 2: 3, 3: 4, 1: 2, 0: 8, 4: 2 }
dct = sorted(dct.items())
print(dct)
#=> [(0, 8), (1, 2), (2, 3), (3, 4), (4, 2)]

dct = { 2: 3, 3: 4, 1: 2, 0: 8, 4: 2 }
for k, v in sorted(dct.items()):
    print(str(k) + ": " + str(v))
    
"""
0: 8
1: 2
2: 3
3: 4
4: 2
"""

#key降順ソート
dct = {2: 3, 3: 4, 1: 2, 0: 8, 4: 2}
for k, v in sorted(dct.items(), key=lambda x: -x[0]):
    print(str(k) + ": " + str(v))

"""
4: 2
3: 4
2: 3
1: 2
0: 8
"""

#value昇順ソート
dct = {2: 3, 3: 4, 1: 2, 0: 8, 4: 2}
dct = sorted(dct.items(), key=lambda x: x[1])
for k, v in sorted(dct.items(), key=lambda x: x[1]):
    print(str(k) + ": " + str(v))

"""
1: 2
4: 2
2: 3
3: 4
0: 8
"""

#value降順ソート
dct = {2: 3, 3: 4, 1: 2, 0: 8, 4: 2}
dct = sorted(dct.items(), key=lambda x: -x[1])
for k, v in sorted(dct.items(), key=lambda x: -x[1]):
    print(str(k) + ": " + str(v))

"""
0: 8
3: 4
2: 3
1: 2
4: 2
"""

#累積和をとる
d = dict(d)
prev = None
for key in d:
    if prev == None:
        prev = key
        continue
    d[key] += d[prev]
    prev = key
    
print(d)

#辞書の値（value）の最大値・最小値を取得
max_v = max(d.values())
print(max_v)
# 100

#辞書の値が最大・最小となるキーを取得
max_k = max(d, key=d.get)
print(max_k)
# a

min_k = min(d, key=d.get)
print(min_k)
# b

#辞書の値が最大・最小となるキーと値を同時に取得
max_kv = max(d.items(), key=lambda x: x[1])
print(max_kv)
# ('a', 100)

print(type(max_kv))
# <class 'tuple'>





