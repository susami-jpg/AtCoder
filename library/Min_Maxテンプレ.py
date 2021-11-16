# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 11:21:50 2021

@author: kazuk
"""

#盤面を埋め終わったときの直大の得点を返す関数
def calc(A):
    score = 0
    #ここに盤面の得点を計算する処理を書く
    return score

#最終局面のターン数(両者が交互に操作した回数)
max_turn = 10

def dfs(A, turn): #A:盤面、turn:どちらのターンか
    if turn == max_turn:
        return calc(A)
    
    #先手
    elif turn%2 == 0:
        max_score = -10*15
        #盤面の状態の列挙
        #下記はoxゲームの一例
        for i in range(3):
            for j in range(3):
                #状態を更新できないならcontinue、更新できるならすべての状態を試す
                if A[i][j] != "*":continue
                A[i][j] = "o" #丸をかく
                #最大スコアの更新
                max_score = max(max_score, dfs(A, turn + 1))
                A[i][j] = "*" #盤面を元に戻す
        return max_score
    
    #後手
    else:
        min_score = 10**15
        #盤面の状態の列挙
        for i in range(3):
            for j in range(3):
                if A[i][j] != "*":continue
                A[i][j] = "x"
                min_score = min(min_score, dfs(A, turn + 1))
                A[i][j] = "*"
        return min_score