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

    def check_intensity_token_composto(self, tokens, i):
    """
    Verifica se há um intensificador (de 1 ou 2 palavras) a partir da posição i.

    Parâmetros:
        tokens (list[str]): Lista de palavras/token já extraídas do texto.
        i (int): Posição atual na lista de tokens.

    Retorna:
        tuple:
            - intensidade (int): 2 se for um intensificador, 1 caso contrário.
            - avanço (int): Número de posições que devem ser puladas no loop.
                           Ex: 1 para palavra única, 2 para composto de duas palavras.
    """

    # 1️⃣ Verifica se o token atual (posição i) é um intensificador simples (ex: "muito")
    palavra = tokens[i].lower()  # Normaliza para minúsculas
    if palavra in self.intensificadores:
        return 2, 1  # Intensificador simples → aplicar intensidade 2, pular 1 token

    # 2️⃣ Verifica se os dois próximos tokens formam um intensificador composto (ex: "pra caramba")
    if i + 1 < len(tokens):  # Garante que há uma próxima palavra
        dupla = f"{tokens[i].lower()} {tokens[i + 1].lower()}"  # Monta a expressão de duas palavras
        if dupla in self.intensificadores:
            return 2, 2  # Intensificador composto → aplicar intensidade 2, pular 2 tokens

    # 3️⃣ Caso não seja intensificador
    return 1, 1  # Intensidade normal (1), pular apenas 1 token


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
