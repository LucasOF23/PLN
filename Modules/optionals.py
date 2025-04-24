#Funções que talvez sejam legais de se ter.
#Esta função é para o caso de encontrar abreviações nas sentenças. Poderia ser uma opção legal de se ter, mas precisa ser melhorada. Como no exemplo abaixo com a função expand_contractions(frase), ainda não traz uma frase certinha.


import re, json
with open('abbreviationsWordlist.json', 'r') as file:
    abbreviationsW_list = json.load(file)


# Function: replace abbreviations to expanded word, in English
def replace_abbreviations(sentence, abbreviationsW_list=abbreviationsW_list):
    for key, value in abbreviationsW_list.items():
        sentence = re.sub(r'(?<!\w)(' + re.escape(key) + r')(?!\w)', value, sentence, flags=re.IGNORECASE)
    sentence = sentence.replace("you.S.", "U.S.")

    return sentence


with open('abbreviationsWordlist.json', 'r') as file:
    abbreviationsW_list = json.load(file)

# contractions_dict = {'didn\'t': 'did not', 'don\'t': 'do not', }
# contractions_re = re.compile('(%s)' % "".join(abbreviationsW_list.keys()))
contractions_re = re.compile('(%s)' % "|".join(map(re.escape, abbreviationsW_list.keys())))

# Function: changes contractions to expanded words, in English
def expand_contractions(sentence, abbreviationsW_list=abbreviationsW_list):
    def replace(match):
        return abbreviationsW_list[match.group(0)]
    return contractions_re.sub(replace, sentence)


#Exemplo:  expand_contractions("U don't need. you've i'm you're haven't a library.") - output: U do not andeed. you have i am yoyou're have not a library.

#Caso seja necessário pra frente, esta função é para o caso de trabalhar com matrizes grandes.

# Function: return a TF-IDF dataframe from dataset sentences
def get_tfidf_v1(sentences, stopwords):
    sentences = sentences.apply(lambda x: replace_abbreviations(x))

    tfidf            = TfidfVectorizer( sublinear_tf = True, #False
                                        min_df = 4,
                                        encoding = 'latin-1', # utf-8 (default)
                                        ngram_range = (1, 3),
                                        stop_words = stopwords )
    X                = tfidf.fit_transform(sentences)
    w_tfidf          = pd.DataFrame()
    w_tfidf['word']  = tfidf.get_feature_names_out()
    w_tfidf['tfidf'] = X.toarray().sum(axis=0)
    w_tfidf.sort_values(by='tfidf', ascending=True, inplace=True)

    return w_tfidf