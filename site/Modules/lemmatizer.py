import spacy

class Lemmatizer:
    def __init__(self, model_name='pt_core_news_sm'):
        try:
            self.nlp = spacy.load(model_name)
        except OSError:
            print(f"Modelo '{model_name}' não encontrado. Execute: python -m spacy download {model_name}")
            raise

    def lemmatize_text(self, text):
        if not isinstance(text, str):
            raise ValueError("A entrada deve ser uma string de texto.")
        
        doc = self.nlp(text)
        print(doc)
        lemmatized_text = " ".join([token.lemma_ for token in doc])
        return lemmatized_text
