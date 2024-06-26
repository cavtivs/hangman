#ハングマンゲーム
def hangman(word): #hangman()関数定義
    wrong = 0 #間違った回数初期化
    stages = ['',
              '               ',
              '_______        ',
              '|              ',
              '|      |       ',
              '|              ',
              '|      O       ',
              '|     /|\\     ',
              '|     / \\     ',
              '|              '
              ]
    rletters = list(word) #引数文字列を分解したリスト
    board = ['_'] * len(word) #wordの文字数文のアンダースカー
    win = False #初期値False
    print('ハングマンへようこそ・・・')

    while wrong < len(stages) -1: #wrongの回数 < stagesの行数(インデックスは0からなので-1)
        print('\n')
        msg = '1文字を予想してくれたまえ・・・：　'
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char) #当たった文字のインデックス
            board[cind] = char #アンダースカーを入力された文字と置き換える
            rletters[cind] = '$' #正解文字リスト側の当たった文字を$と置き換える(.index()は最初のマッチしか返さないから)
        else:
            wrong += 1 #間違った回数インクリメント
        print(' '.join(board)) #boardに空白文字を足したのをプリント
        e = wrong + 1 #インデックス数+1
        print('\n'.join(stages[0 : e])) #間違った回数分の行のハングマンを出力
        if '_' not in board:
            print('ぐぬ・・・うまくやりおったな・・・。')
            print(' '.join(board))
            win = True
            break
    if not win: #winが偽なら
        print('\n'.join(stages[0 : wrong +1]))
        print('残念だったなァ・・正解は{}だよォ。イヒヒヒ！'.format(word)) #print(f' ')でも可

import random
secret_words = ['dog', 'cat', 'snake', 'mouse',  'cow', 'rabit', 'dragon', 'snake', 'hen', ]
w = secret_words[random.randint(0, 8)]
hangman(w)
