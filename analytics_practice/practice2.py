
'''
# Q1: 1から50までの和を計算して表示
k = 0
for i in range(1,51):
     k += i
print(k)
'''


'''
# Q2: 1000以下の素数を計算して表示せよ
素数 = 1より大きい整数で、1とその数自身以外のどの自然数でも割り切れない数
for i in range(2,1001):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
            print(i)

'''


"""
Q3: フィボナッチ数列を表示せよ
２つ前と１つ前の数の和になる数列
1,1,2,3,5,8,13...

a = 0
b = 1
for i in range(10):
    print(b)
    a,b=b,a+b
"""


"""
Q4: 2つの自然数の最小公倍数/最大公約数を表示せよ（ユークリッドの互除法）
最小公倍数：二つの変数の共通な倍数のうち最小なもの
最大公約数：二つの変数に共通な約数のうち最大のもの

a = 16
b = 6
#最大公約数
def gcd(a,b):
    if b == 0 :
        return a
    else:
        return gcd(b,a%b)
xcd = gcd(a,b)
print(xcd)
#最小公倍数
lcm = a*b / xcd
print(lcm)
"""


"""
Q5: 0から100の内３の倍数と３のつく数字だけ表示せよ。

for i in range(0,101):
    if i % 3 == 0 or "3" in str(i):
        print(i)
"""


"""
Q6: 問題：1〜100までの数字のうち、3で割り切れるものは"Fizz!",5で割り切れるものは"Buzz!",15で割り切れるものは"FizzBuzz!"と表示させ、
それ以外の数はそのままの数を表示させなさい。

for i in range(1,101):
    if i % 3 ==0:
        print("Fizz!")
    elif i % 5 == 0:
        print("Buss!")
    elif 1 % 15 == 0:
        print("FizzBuzz!")
    else:
        print(i)
　　
"""


"""
Q7: その内整数nまでの”z”の個数を計算し表示せよ（ただしif文,for文の使用不可）
問題：Q６と同じ規則に従って、1から整数nまでを数字,Fizz,Buzz,FizzBuzz,に分けていき、その内いくつ"z"があるか個数をカウントし表示させなさい。
条件：if文,for文は使用してはいけない。

def z_count(n):
    print((n // 3*2)+(n // 5*2))

z_count(15)
"""


"""
Q8:　為替自動換算クラスの作成
問題：日本円をドルとユーロに換算するクラスを作成せよ。
条件：・1ドル=109円, 1ユーロ=129円で換算。(2018/5/8現在)
　　　・クラスの引数に日本円を入力して、その後その値を各通貨に換算できるようする。

class Yen_Doll_Uro:
    def __init__(self,yen):
        self.yen = yen

    def doll(self):
        doll = self.yen / 91
        return (doll)

    def uro(self):
        uro = self.yen / 78
        return(uro)

exchange = Yen_Doll_Uro(300)
print('日本円で300円は'+str(exchange.doll())+'ドルです')
print('日本円で300円は'+str(exchange.uro())+'ユーロです')

"""



"""

Q9: RPGゲームクラスの作成
問題：キャラクターのステータスを登録して、お互いに攻撃することができるクラスを
　　　作成せよ。
条件：・キャラクターは名前,体力の現在値、体力の最大値、攻撃力,防御力の
　　　　5つのパラメータをもっており、いつでも参照することができる。
　　　・キャラクターは別のキャラクターを攻撃して、
　　　　相手の体力を自分の攻撃力(-相手の防御力)分だけ減らすことができる。

少し長いクラスの作成となります。




class Character:
    def __init__(self, name, max_hp, attack_power, defence_power):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.attack_power = attack_power
        self.defence_power = defence_power

    def status(self):
        return "{}: 体力{}/{} 攻撃力{} 防御力{}".format(self.name, self.hp, self.max_hp, self.attack_power, self.defence_power)

    def attack(self, enemy):
        attacked = self.attack_power - enemy.defence_power
        enemy.hp -= attacked
        return "{}が{}に攻撃！{}のダメージ".format(self.name, enemy.name, attacked)


yusha = ("勇者", 60, 10, 2)
slime = ("スライム", 15, 5, 1)

# 現在のステータスを表示
print(yusha.status())
print(slime.status())

# 双方の攻撃
yusha.attack(slime)
slime.attack(yusha)

# 双方の攻撃後のステータスを表示
print(yusha.status())
print(slime.status())
"""



"""
Q10 Hashnumber 判定
問題：整数 X の各桁の数字の和を f(X) としたとき、
　　　X が f(X) で割り切れる場合、X はハーシャッド数です。
　　　整数 N が与えられるので、ハーシャッド数かどうか判定してください。

str()や,map()やsum()を使う良い練習になるのではないでしょうか。


def c_hassh(n):
    s = str(n)
    array = list(map(int, list(s)))
    sum_x = sum(array)
    if n % sum_x ==0:
        print('Hashnumber')
    else:
        print('Not Hashnumber')

c_hassh(10)
"""

"""
Q12: テキストファイル内で指定した文字がいくつ含まれているか数える

print(open("sample.txt").read().count("い"))
"""


"""
Q13: 摂氏と華氏を自動変換
問題：摂氏（℃）を入力すると華氏（°F）に変換し表示し、
　　　華氏を入力すると摂氏に変換表示してくれる関数を作成せよ。
条件：摂氏の場合は"26C"のように入力し、華氏の場合は"67F"のように入力する。

文字列（リスト）の最後の文字をどう取ってくるか。最後以外をどう取ってくるかの練習になりますね。

def convert(text):
    # fだったらfの温度から-32 / 1.8
    if text[-1] == "F":
        fel = int(text[:-1])
        awnser = (cel -32) / 1.8
    # cだったらcの温度から* 1.8 + 32
    elif text[-1] == "C":
        cel = int(text[:-1])
        awnser = cel * 1.8 +32
    else:
        awnser = '正しく入力してください'
    return awnser

print(convert("65C"))
"""


"""
Q14入れ子のリストを平らにする
問題：[[1,2],3,4,5,[6,[7,[8,9]]]]のように入れ子になっているリストを、
　　　[1, 2, 3, 4, 5, 6, 7, 8, 9]のように平らに入れ直したい。

def list_flatter(lst):
    r = []
    for i  in lst:
        if type(i) is list:
            r.extend(list_flatter(i))
        else:
            r.append(i)
    return r

list_a = [1,2],3,4,5,[6,[7,[8,9]]]
print(list_flatter(list_a))
"""


"""
Q15: 対話型残業代自動算出システム
問題：「現在の時刻」「定時」「1時間あたりの残業代」を対話式に入力すると、
　　　　残業代が自動で表示されるシステムを作れ。
条件：時刻の入力は”17:00”のように入力される。
対話型の練習
"""


print("現在の時刻を「20:13」のように入力してください")
current_time = input(">>")
print("定時を「19:00」のように入力してください")
out_time = input(">>")
print("１時間あたりの残業代(円)を「1500」のように入力してください")
hour_money = float(input(">>"))
# 現在時刻の計算
current_h = float(current_time[0:2])
current_m = float(current_time[3:5])
# 以上を分に統一する
current_time_min = (current_h * 60) + current_m

# 定時の計算
out_time_h = float(out_time[0:2])
out_time_m = float(out_time[3:5])
# 以上を分に統一する
out_time_min = (out_time_h * 60) + out_time_m

# 残業時間の計算
leave_time_min = current_time_min - out_time_min
# 1時間単位に直す(roundで小数点以下第二位まで丸め込む)
leave_time_h = round((leave_time_min / 60), 2)
leave_time_mony = leave_time_h * hour_money
print("あなたの残業時間は{0}時間です。あなたの残業代は{1}です。".format(leave_time_h, leave_time_mony))
