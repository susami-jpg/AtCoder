# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 19:37:15 2021

@author: kazuk
"""

def levenshtein_distance(a, b):
    m = [ [0] * (len(b) + 1) for i in range(len(a) + 1) ]

    for i in range(len(a) + 1):
        m[i][0] = i

    for j in range(len(b) + 1):
        m[0][j] = j

    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                x = 0
            else:
                x = 1
            m[i][j] = min(m[i - 1][j] + 1, m[i][ j - 1] + 1, m[i - 1][j - 1] + x)
    # print m
    return m[-1][-1]

"""
apple
play
という二つの単語の編集距離 LD("apple", "play") を求めます。

このとき、apple, play それぞれの一文字前までの編集距離として以下の3通りが考えられます

LD("appl", "play")
LD("apple, "pla")
LD("appl", "pla")
これらの値が既に既知であったとしましょう。LD("apple", "play") を求めるのに、うまくこの 3 つの値を使うことを考えます。つまり、既に分かっている直前の部分問題の最適解に {挿入, 削除, 置換} いずれかの操作を加えて LD("apple", "play") の最適解を求めるのです。

LD("appl", "play") に "e" を挿入(+1)で LD("apple", "play") になる → LD("apple", "play") = LD("appl", "play") + 1
LD("apple, "play") から "y" を削除で LD("apple", "pla") になる、すなわち LD("apple", "pla") は削除操作一回(+1)で LD("apple", "play") と同じ → LD("apple", "play") = LD("apple", "pla") + 1
LD("appl", "pla") の次の文字を置換 (+1) で LD("apple", "play") になる → LD("apple", "play") = LD("appl", "pla") + 1
ただし、次の文字が等しい場合は置換の必要がない → 例 LD("apple", "plane") = LD("appl", "plan") + 0
これらの関係から、LCS長の時同様、再帰的な漸化式が得られそうなのは直感的に分かります。上記3パターンを i 番目, j 番目までの編集距離 LD(i, j) で一般化してみます。

LD(i, j) = LD(i - 1, j) + 1
LD(i, j) = LD(i, j - 1) + 1
LD(i, j) = LD(i - 1, j - 1) + α, ただし α = 0 または 1 (i, j 番目の文字が等しい場合は 0)
となります。編集距離は最小手順ですから、最適解はこの3つの値のうち最小のものになります。結局 LD(i, j) を求めるには LD(i - 1, j -1), LD(i - 1, j), LD(i, j -1) が分かっていれば良いことが分かります。予想通り、再帰的な漸化式になっています。DP 的には、ここまで来ればあとは簡単です。

i, j は任意ですので LD(i - 1, j -1), LD(i - 1, j), LD(i, j -1) もまたより小さな LD(i', j') から求まります。つまり編集距離 LD(i, j) を求めるには部分問題の最適解を再帰的に求めていくことで計算できるわけです。なお、LD(0, 0) = 0, LD(i, 0) = i, LD(0, j) = j なのは自明です。

これらの考え方により、結果として DP のよくあるパターン、

i行j列の2次元の表を用意して
自明な既知の値 (今回は LD(0, 0) = 0, LD(i, 0) = i, LD(0, j) = j) を基点に
i, j の昇順に既知の値だけを使って最適解 (編集距離では最小値) を計算していく
最適解 … 2次元の表の min{左 + 1, 上 + 1, 左上 + if (i番目j番目の文字が等しい) then 0 else 1 }
で編集距離が求まることが分かります。
"""