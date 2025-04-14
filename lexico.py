import numpy
import pandas
import scipy
import sklearn


class Lexico:

    def __init__(self, nome_lexico):
        # Defines 3 dictionaries, one for the tags and the other 2 for the words:
        # - self.tags has each tag classification (-1 neg, 0 neu, 1 pos)
        # - self.classified_dictionary has each word classification (-1 neg, 0 neu, 1 pos)
        # - self.dictionary has each word and its tags

        # Open Lexicon

        f = open(nome_lexico, "r")

        # Reading Tags

        if(f.readline() == "%\n"):

            self.tags = dict()

            line = f.readline()
            while(len(line) > 2):
                words = line.split()
                self.tags[int(words[0])] = int(words[2])
                # print(words)
                line = f.readline()
            # print(self.tags)
        else:
            print("error")

        # Reading Dictionary

        line = f.readline()

        self.classified_dictionary = dict()
        self.dictionary = dict()

        while(len(line) > 0):
            words = line.split()
            # print(words)
            sum = 0
            for i in words[1:]:
                sum = sum + self.tags[int(i)]
            if(sum < -1):
                sum = -1
            if(sum > 1):
                sum = 1
            self.classified_dictionary[words[0]] = sum
            self.dictionary[words[0]] = words[1:]
            line = f.readline()
        
        # print(self.dictionary)

    '''
    def classify_token(self, word):
        # Receives a token and returns -1 if negative, 0 if neutral and 1 if positive

    def check_intensity_token(self, word):
        # Check if this token indicates intensity for the next one, returns 1 if false and 2 if true

    def tokenization(self, text):
        # Takes text and creates a self.tokens (vector with tokens)
        self.tokens

    def remove_stopword(self):
        # Remove tokens that dont help in classification (words with specific tags can be taken out)

    # def lematization or stemming, dont know if the lexicon is adapted to that, but can be made

    def classify_text(self, text = "Nothing here\n", text_file = None):
        # Receives a text or a file name and classify that text in Positive, Neutral or Negative

        if(text_file != None):
            # Read file into text

        # Tokenization
        self.tokenization(text)

        # Remove Stop Word
        self.remove_stopword()

        # Classify tokens
        intensity = 1
        value = 0
        for i in self.tokens:
            value += intensity * self.classify_token(i)
            intensity = self.check_intensity_token(i)

        # Print Results
        if(value > 0):
            print("Positive")
        
        if(value < 0):
            print("Negative")

        if(value == 0):
            print("Neutral")
    '''
