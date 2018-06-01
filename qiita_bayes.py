#coding:utf-8
# http://gihyo.jp/dev/serial/01/machine-learning/0003 のベイジアンフィルタ実装をPython3.3向けにリーダブルに改良
import math
import sys
import MeCab


class NaiveBayes():
    def __init__(self):
        self.vocabularies = set() #単語の(?)集合。リストとは異なり、順番はない。
        self.word_count = {}  # {'category': {'word1': 4, 'word2': 2,...} }
        self.category_count = {}  # {'cateogry': 16, ...}

    def to_words(self, sentence):
        """
        入力: 'すべて自分のほうへ'
        出力: tuple(['すべて', '自分', 'の', 'ほう', 'へ'])
        """
        tagger = MeCab.Tagger('mecabrc')  # 別のTaggerを使ってもいい
        mecab_result = tagger.parse(sentence)   #引数sentense(=document)を分解したものをmecab_resultに代入
        info_of_words = mecab_result.split('\n')    #改行文字で区切ったものをinfo_of_wordsに代入
        words = []
        for info in info_of_words:
            # macabで分けると、文の最後に’’が、その手前に'EOS'が来る
            if info == 'EOS' or info == '':
                break
                # info => 'な\t助詞,終助詞,*,*,*,*,な,ナ,ナ'
            info_elems = info.split(',')
            # 6番目に、無活用系の単語が入る。もし6番目が'*'だったら0番目を入れる
            if info_elems[6] == '*':
                # info_elems[0] => 'ヴァンロッサム\t名詞'
                words.append(info_elems[0][:-3])    #リストオブジェクト.append(オブジェクト)　リストの最後に指定したオブジェクトを追加
                continue
            words.append(info_elems[6])
        return tuple(words)  #tuple() リストからタプルに変換する

    def word_count_up(self, word, category):
        self.word_count.setdefault(category, {})    #setdefault(,) の説明 http://d.hatena.ne.jp/kuma8/20090429/1241012846
        self.word_count[category].setdefault(word, 0)   #ex)wordがword_count[category]にあったらそれを表示、なかったら0を表示
        self.word_count[category][word] += 1    #categoryとwordのリストの数を更新
        self.vocabularies.add(word) #vocabulariesにwordを追加

    def category_count_up(self, category):
        self.category_count.setdefault(category, 0)
        self.category_count[category] += 1

    def train(self, doc, category):
        words = self.to_words(doc)  #wordsにto_wordsメソッドを代入(=文章をparseしたものを代入)
        for word in words:  #リストwordsの内容をwordに代入していき、リストwordsの数だけ繰り返し処理を行う
            self.word_count_up(word, category)
        self.category_count_up(category)

    def prior_prob(self, category): #事前確率
        num_of_categories = sum(self.category_count.values())   #変数名.values()　辞書(__init__で定義したself.category_count = {})の値を取ってくる
        num_of_docs_of_the_category = self.category_count[category] #category_countのcategoryリスト(の数?)を代入する
        return num_of_docs_of_the_category / num_of_categories  ###そのカテゴリ内にその文書があった数をカテゴリの数で割っている　＝　

    def num_of_appearance(self, word, category):
        if word in self.word_count[category]:   # if 「検索する文字列」 in 「検索される文字列」:    categoryがword_countの中にあれば....
            return self.word_count[category][word]  #categoryリストの数とwordリストの数を返す
        return 0

    def word_prob(self, word, category):
        # ベイズの法則の計算。(=事後確率)通常、非常に0に近い小数になる。
        numerator = self.num_of_appearance(word, category) + 1  # +1は加算スムージングのラプラス法　　分子
        denominator = sum(self.word_count[category].values()) + len(self.vocabularies)  #分母

        # Python3では、割り算は自動的にfloatになる
        prob = numerator / denominator  #分子/分母
        return prob

    def score(self, words, category):
        # logを取るのは、word_probが0.000....01くらいの小数になったりするため
        score = math.log(self.prior_prob(category)) #事前確率に対してlogをとっている
        for word in words:  #wordsの中にあるwordに対して
            score += math.log(self.word_prob(word, category))   #事後確率に対してlogをとったものをscoreに代入
        return score

    # logを取らないと値が小さすぎてunderflowするかも。上のメソッドのlogをとっていないvar.
    def score_without_log(self, words, category):
        score = self.prior_prob(category)
        for word in words:
            score *= self.word_prob(word, category)
        return score

    def classify(self, doc):
        best_guessed_category = None
        max_prob_before = -sys.maxsize  ###事後確率の最大値.全てのカテゴリの中での最大スコアのものが、最も尤度の高いカテゴリであると判断し、最終的にそのカテゴリを出力する。  -はどういう意味？
        words = self.to_words(doc)  #wordsに以下で入力するdocを分解したものを代入

        for category in self.category_count.keys(): ###category_countのkeyを呼び出して
            prob = self.score(words, category)  #wordsとcategoryのscoreをprobに代入
            if prob > max_prob_before:  #probがmax_prob_before(=事後確率の最大値)よりも大きければ
                max_prob_before = prob  #max_prob_beforeにprobを代入する
                best_guessed_category = category    #categoryをcategory尤度(=最もそれらしいカテゴリ)として代入。
        return best_guessed_category    #最もそれらしいカテゴリを返す

if __name__ == '__main__':  # http://programming-study.com/technology/python-if-main/  端的にはモジュールとして呼び出すのではなく、直接同ファイル内で使用する際の宣言的なもの(?)
    nb = NaiveBayes() #NaiveBayesクラスを呼び出す
    nb.train('''Python（パイソン）は，オランダ人のグイド・ヴァンロッサムが作ったオープンソースのプログラミング言語self.
                オブジェクト指向スクリプト言語の一種であり，Perlとともに欧米で広く普及している。イギリスのテレビ局 BBC が製作したコメディ番組『空飛ぶモンティパイソン』にちなんで名付けられた。
                Python は英語で爬虫類のニシキヘビの意味で，Python言語のマスコットやアイコンとして使われることがある。Pythonは汎用の高水準言語である。プログラマの生産性とコードの信頼性を重視して設計されており，核となるシンタックスおよびセマンティクスは必要最小限に抑えられている反面，利便性の高い大規模な標準ライブラリを備えている。
                Unicode による文字列操作をサポートしており，日本語処理も標準で可能である。多くのプラットフォームをサポートしており（動作するプラットフォーム），また，豊富なドキュメント，豊富なライブラリがあることから，産業界でも利用が増えつつある。
             ''',
             'Python')
    nb.train('''ヘビ（蛇）は、爬虫綱有鱗目ヘビ亜目（Serpentes）に分類される爬虫類の総称。
                体が細長く、四肢がないのが特徴。ただし、同様の形の動物は他群にも存在する。
                ''', 'Snake')
    nb.train('''Ruby（ルビー）は，まつもとゆきひろ（通称Matz）により開発されたオブジェクト指向スクリプト言語であり，
                従来 Perlなどのスクリプト言語が用いられてきた領域でのオブジェクト指向プログラミングを実現する。
                Rubyは当初1993年2月24日に生まれ， 1995年12月にfj上で発表された。
                名称のRubyは，プログラミング言語Perlが6月の誕生石であるPearl（真珠）と同じ発音をすることから，
                まつもとの同僚の誕生石（7月）のルビーを取って名付けられた。
             ''',
             'Ruby')
    nb.train('''ルビー（英: Ruby、紅玉）は、コランダム（鋼玉）の変種である。赤色が特徴的な宝石である。
                天然ルビーは産地がアジアに偏っていて欧米では採れないうえに、
                産地においても宝石にできる美しい石が採れる場所は極めて限定されており、
                3カラットを超える大きな石は産出量も少ない。
             ''', 'Gem')    #このtrainメソッドの第一引数に、タイトルなどを入れる。第二引数に、カテゴリを入れる。
    doc = 'グイド・ヴァンロッサムが作ったオープンソース'  #ここにurlを入れる→形態素解析も
    print('%s => 推定カテゴリ: %s' % (doc, nb.classify(doc)))  # 推定カテゴリ: Pythonになるはず
    print('Pythonカテゴリである確率: %s' % nb.score(['グイド・ヴァンロッサム', 'が', '作った'], 'Python'))
    print('Rubyカテゴリである確率: %s' % nb.score(['グイド・ヴァンロッサム', 'が', '作った'], 'Ruby'))

    doc = 'プログラミング言語のRubyは純粋なオブジェクト指向言語です.'
    print('%s => 推定カテゴリ: %s' % (doc, nb.classify(doc)))  # 推定カテゴリ: Rubyになるはず
    print('Rubyカテゴリである確率: %s' % nb.score(['プログラミング言語', 'の', 'Ruby', 'は', '純粋', 'な', 'オブジェクト指向言語', 'です', '。'], 'Ruby'))
    print('Pythonカテゴリである確率: %s' % nb.score(['プログラミング言語', 'の', 'Ruby', 'は', '純粋', 'な', 'オブジェクト指向言語', 'です', '。'], 'Python'))

    doc = 'コランダム'
    print('%s => 推定カテゴリ: %s' % (doc, nb.classify(doc)))  # 推定カテゴリ: Gemになるはず
    print('Gemカテゴリである確率: %s' % nb.score(['コランダム'], 'Gem'))
    print('Rubyカテゴリである確率: %s' % nb.score(['コランダム'], 'Ruby'))
