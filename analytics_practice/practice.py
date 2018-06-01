"""
1問目：空のリストx1に1~10までの値をfor文で追加して下さい。
"""
list = []
for i  in range(1,11):
    list.append(i)
print(list)



"""
2問目：リストx2に1~10までの値を内包表記で追加して下さい。
"""
list2 = [i for i in range(1,11)]
print(list2)



"""
３問目： a = [1,3,5,7,9,11] というリストのインデックス（行番号）と値を以下のように出力
"""
a = [1,3,5,7,9,11]
for i,j in enumerate(a):
    print(i,j)


"""
４問目： a = [1,2,3,4,5], b=[6,7,8,9,10], c=[11,12,13,14,15] の同じ行同士の値の掛け算を出力
"""
a = [1,2,3,4,5]
b=[6,7,8,9,10]
c=[11,12,13,14,15]

for a_val,b_val,c_val in zip(a,b,c):
    print(a_val*b_val*c_val)

"""
5問目：以下のnumsというリストにおいて、７で割り切れない値のみを出力してください。
"""
nums = [4, 11, 14, 18, 25, 28, 70, 97,105]
for num in nums:
    if num % 7 != 0:
        print(num)

"""
6問目：以下のnumsというリストにおいて、７で割り切れない値のみをanswers1というリストに追加してください。（for文を用いて）
"""
answers1 = [num for num in nums if num % 7 != 0]
print(answers1)


"""
7問目：以下のnumsというリストにおいて、７で割り切れない値のみをanswers2というリストに追加してください。（内包表記を用いて）
"""
answers2 = []
for num in nums:
    if num % 7 != 0:
        answers2.append(num)
print(answers2)



"""
8問目：以下に科目ごとの点数が入ったscoresというリストがあります。科目ごとの点数をリストjapanese,english,mathにそれぞれ格納して下さい。（for文を用いて）
"""
scores = [{'国語': 50, '英語': 82, '数学': 67},
          {'国語': 52, '英語': 62, '数学': 60},
          {'国語': 15, '英語': 84, '数学': 35},
          {'国語': 75, '英語': 42, '数学': 68},
          {'国語': 66, '英語': 92, '数学': 27},
          ]
japanese = []
english = []
math = []

for score in scores:
    japanese.append(score['国語'])
    english.append(score['英語'])
    math.append(score['数学'])
print(japanese)


"""
9問目：以下に科目ごとの点数が入ったscoresというリストがあります。科目ごとの点数をリストjapanese,english,mathにそれぞれ格納して下さい。（内包表記を用いて）
"""
japanese = [score['国語'] for score in scores]
english = [score['英語'] for score in scores]
math = [score['数学'] for score in scores]
print(japanese)

