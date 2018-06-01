import sys


class NaiveBayes()
    def __init__(self,document,category):
        self.word_count = {}  #{'category'{ 'word1':3, 'word2':4, .....}}
        self.category_count = {}  #{'category':12, ....}
        self.vocabularies = set()

    def to_word(self,sentence): #形態素解析
        """
        MeCabで形態素解析。tapleで表示されるようにする
        入力:私はいけ
        出力：tuple(['私'　,'は',　'いけ'])
        """
        tagger = MeCab.tagger('mecabrc')
        mecab_result = tagger.parse(sentence)
        words_split = mecab_result.split('\n')
        words = []
        for i in words_split
            if i == 'EOS' or i == '':
                break
            i_elms = info.split(',')

            if info_elms[6] == '*':
                words.append(i_elms[0][:3])
                continue
            words.append(i_elms[6])
        return tuple(words)

    def word_count_up(self,word,category):
        self.word_count_up.setdefault(category,{})
        self.word_count_up[category].setdefault(word,0)
        self.word_count_up[category][word] += 1
        self.vocabularies.add(word)

    def category_count_up(self,category):
        self.category_count.setdefault(category,0)
        self.category_count[category] += 1

    def train(self,doc,category):
        words = self.to_words(doc)
        for word in words:
            self.word_count_up(word,category)
        self.category_count_up(category)

    def prior_prob(self,category):  #事前確率
        sum_of_categories = sum(self.category_count_up.values())
        num_of_the_category = self.category_count[category]
        return num_of_the_category / sum_of_categories

    def num_of_appearance(self,word,category):  #尤度
        if word in self.word_count[category]:
            return self.word_count[category][word]
        return 0

    def word_prob(self,word,category):
        numerator = self.num_of_appearance(word,category) + 1
        denominator = sum(self.word_count[category].values() + len(self.vocabularies))
        prob = numerator / denominator
        return prob

    def score(self,word,category):
        score = math.log(self.prior_prob(category))
        for word in words:
            score *= math.log(self.word_prob(word,cateogry))
        return score

    def classify(self,doc):
        best_guessed_category = None
        max_prob_before = -sys.maxsize
        words = self.to_words(doc)

        for category in self.category_count.key():
            prob = self.score(words,category)
            if prob > max_prob_before:
                max_prob_before = max_prob_before
                best_guessed_category = category
        return best_guessed_category

if __name__ == '__main__':
    nb = NaiveBayes()
    nb.train('''私は池本加奈です。埼玉県吉川市平沼に住んでいます。
                好きな食べ物は肉です。趣味は本を読むことと寝ることと、少し走ることとお茶を飲むこと。
                どうぞよろしく。
             ''',
             '池本加奈'
             )
    nb.train('''
             私は池本さきです。25歳のOLです。趣味はカフェ巡りと、写真、ダイビングも時々やります。
             ''',
             'saki'
             )
    
