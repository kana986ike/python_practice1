#-*- coding:utf-8 -*-
#これは受け取ったurlのテキストを形態素解析するモジュール
# http://tech.innovation.co.jp/2017/07/28/mecab.html  今回は「キーワード」を抽出したいので、品詞が「名詞」のもののみ出力させる。

import re
import bs4
import sys
import MeCab
import urllib.request
from pprint import pprint

#指定したURLをセット
if len(sys.argv) == 2:  #コマンドラインで渡される引数が入ったリスト。 http://uxmilk.jp/8676 len(sys.argv)で引数の数をカウントできる。
    url = sys.argv[1]
else:
    print("URLを指定してください")
    exit()
                                                                            #bs4モジュール内のBeautifulSoupクラスを呼び出し
soup = bs4.BeautifulSoup(urllib.request.urlopen(url).read(),"html.parser")  #http://www.shibuya24.info/entry/beautifulsoup
                                                                            #urllib.requestはurlを取得するためのpythonモジュール
                                                                            #urlopen()はurlを開く。read()はテキストを全て読み込む
#title,description,h1を抜き出し、処理対象としてセット
title = soup.title.string
description = soup.find( attrs={'name': re.compile(r'Dscripution', re.I)} ) .attrs['content']    #https://tdoc.info/beautifulsoup/#findall-name-none-attrs-recursive-true-text-none-limit-none-kwargs attrsはキーワード引数と同じように辞書型として振る舞います。
h1 = soup.h1.string # re.compile():正規表現パターンを 正規表現オブジェクト にコンパイルします。.string:内部テキストにアクセスできるここではsoupにてparseしたhtmlのh1をh１に代入
contents = title + description + h1
output_words = []

#MeCabでキーワードを抽出する
m = MeCab.Tagger()
keywords =m.parse(contents)

for row in keywords.split("\n"): #split()関数。文字列を開業で分割。
    word = row.split("\t")[0]
    if word == "EOS":
        break
    else:
        pos = row.split("\t")[1].split(",")[0]
        if pos == "名詞":
            output_wods.append(word)

#ユニークにして出力
pprint(list(set(output_wods)))  #output_words[]をset()で重複した要素を取り除いている。タプルからリストに変換するため list()で縦に並べる
