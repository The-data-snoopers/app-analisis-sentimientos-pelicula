from collections import Counter
import unicodedata
from sklearn.base import BaseEstimator, TransformerMixin
from nltk.corpus import stopwords
import pandas as pd
import nltk
import enchant
import re


class TextPreprocessor(BaseEstimator, TransformerMixin):
    def __init__(self):
        print("Reviews initialized")
        self.en_us = enchant.Dict("en_US")
        self.palabras_no_existe = []


    def fit(self, X, y=None):
        print("Fitting reviews...")
        return self

    def transform(self, X, y=None):
        print("Transforming reviews...")
        return self.preprocess(X)

    def verificar_palabra(self,text):
        
        """and self.es_es.check(word) == False"""
        for word in text.split(" "):
            if self.en_us.check(word)== False :
                if word not in self.palabras_no_existe:
                    self.palabras_no_existe.append(word)
        return self.palabras_no_existe

    def preprocess(self, df:pd.DataFrame) -> pd.DataFrame:
        print("Preprocessing text...")
        # convert series to dataframe
        movies_df = pd.DataFrame(df)


        # Descargando las stopwords
        nltk.download('stopwords')
        stop_words = list(stopwords.words('spanish'))
        stop_words_e = list(stopwords.words('english'))

        # Eliminando caracteres no alfanumericos y pasamos los caracteres a minusculas
        movies_df['review_es'] = movies_df['review_es'].apply(lambda x: re.sub(r'\W+', ' ', x).lower())

        # Eliminamos las stopwords de español y ingles
        movies_df['review_es'] = movies_df['review_es'].apply(lambda x: " ".join([word for word in x.split() if word not in stop_words]))
        movies_df['review_es'] = movies_df['review_es'].apply(lambda x: " ".join([word for word in x.split() if word not in stop_words_e]))

        #Eliminamos las palabras que no pertenecen al Español ni Inglés
        lista_correcciones =  []
        for value in movies_df['review_es']:
            for word in self.verificar_palabra(value):
                lista_correcciones.append(word)
        text=r'\b(' + '|'.join(lista_correcciones) + r')\b'
        movies_df['review_es'] = movies_df['review_es'].apply(lambda x: re.sub(text,' ', x))

        #Remover las palabras con poca frecuencia de apariciones
        word_count = Counter()
        for text in movies_df['review_es']:
            for word in text.split():
                word_count[word] += 1
        RARE_WORDS = set(word for (word, wc) in word_count.most_common()[:-10:-1])
        movies_df['review_es'] = movies_df['review_es'].apply(lambda x: " ".join([word for word in x.split() if word not in RARE_WORDS]))

        # Remover las palabras con alta frecuencia de apariciones
        FREQUENT_WORDS = set(word for (word, wc) in word_count.most_common(10))  
        movies_df['review_es']= movies_df['review_es'].apply(lambda x: " ".join([word for word in x.split() if word not in FREQUENT_WORDS]))
        
        # Eliminamos las tildes
        movies_df['review_es'] = movies_df['review_es'].apply(lambda x: ''.join(c for c in (unicodedata.normalize('NFD', x)) if unicodedata.category(c) != 'Mn'))
        print("data: ",movies_df)
        movies = movies_df['review_es']
        print("Finished preprocessing text...")


        return movies