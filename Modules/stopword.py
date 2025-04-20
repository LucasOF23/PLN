import numpy as np
import nltk
from nltk.stem.porter import *
import spacy, gensim, string
import regex as re, unicodedata
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

class Stopword_RMV:

    #Primeiramente, crio uma lista mais completa de stop-words (tanto em Ingles quanto em Portugues), somando as listas existentes e obtendo uma lista com unique words. Caso saibam de alguma outra me avise para que eu coloque junto. 
    def __init__(self, pt = True):
        if(pt):
            self.stop_words = self.sw_pt()
        else:
            self.stop_words = self.sw_en()

    # Function: returns an English stop-words list
    def sw_en(self):
        # loading en_lang model in gensim package  (size = 337)
        gensim_en = gensim.parsing.preprocessing.STOPWORDS
        # loading en_lang small model in spacy package (size = 326)
        en = spacy.load('en_core_web_sm')
        spacy_en = en.Defaults.stop_words
        # loading en_lang model in nltk package  (size = 179)
        nltk_en = nltk.corpus.stopwords.words('english')
        # adding all in one list
        sw = nltk_en.copy()
        sw.extend(['http', 'https', 'www', 'youtube', '#', '@', '[()]', '[‘’“”…,]', 'â€˜'])
        sw.extend(spacy_en)
        sw.extend(gensim_en)
        sw = np.unique(sw)
        #print('StopWords_en: size = %d.' % len(sw))

        sw.tolist()

    # Function: returns a Portuguese stop-words list
    def sw_pt(self):
        # loading pt_lang small model in spacy package (size = 416)
        pt = spacy.load('pt_core_news_sm')
        spacy_pt = pt.Defaults.stop_words
        # loading pt_lang model in nltk package  (size = 207)
        nltk_pt = nltk.corpus.stopwords.words('portuguese')
        # adding all in one list
        #sw = nltk_pt.copy()
        sw = []
        sw.extend(['http', 'https', 'www', 'youtube', '#', '@', '[()]', '[‘’“”…,]', 'â€˜'])
        sw.extend(spacy_pt)
        sw = np.unique(sw)
        #print('StopWords_pt: size = %d.' % len(sw))

        return sw.tolist()

    # Function: returns a cleaned sentence removing stopwords
    def remove_stopwords(self, tokens):

        # remove stopwords, digits, special caracters and punctuation
        v = [word for word in tokens if not word in self.stop_words and word.isalnum() and not word.isdigit()]

        return v

