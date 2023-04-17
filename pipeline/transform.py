from sklearn.base import BaseEstimator, TransformerMixin
from nltk.corpus import stopwords
import pandas as pd
import nltk
import enchant
import re
import language_tool_python



class TextPreprocessor(BaseEstimator, TransformerMixin):
    def __init__(self):
        print("Reviews initialized")
        self.en_us = enchant.Dict("en_US")
        self.es_es = enchant.Dict("es_ES")
        self.palabras_no_existe = []
        """
        self.stop_words = set(stopwords.words('english'))
        nltk.download('stopwords')
        self.stop_words = list(stopwords.words('spanish'))
        self.stop_words_e = list(stopwords.words('english'))"""

    def fit(self, X, y=None):
        print("Fitting reviews...")
        return self

    def transform(self, X, y=None):
        print("Transforming reviews...")
        return self.preprocess(X)

    def verificar_palabra(self,text):

        for word in text.split(" "):
            if self.en_us.check(word)== False and self.es_es.check(word) == False:
                if word not in self.palabras_no_existe:
                    self.palabras_no_existe.append(word)
        return self.palabras_no_existe

    def preprocess(self, df: pd.DataFrame) -> pd.DataFrame:
        print("Preprocessing text...")
        # convert series to dataframe
        movies_df = pd.DataFrame(df)

        # Descargando las stopwords
        nltk.download('stopwords')
        stop_words = list(stopwords.words('spanish'))
        stop_words_e = list(stopwords.words('english'))

        movies_df = movies_df.drop('Unnamed: 0', axis=1)
        
        # Eliminando caracteres no alfanumericos y pasamos los caracteres a minusculas
        movies_df['review_es'] = movies_df['review_es'].apply(lambda x: re.sub(r'\W+', ' ', x).lower())
        
        # Eliminamos las stopwords de español y ingles
        movies_df['review_es'] = movies_df['review_en'].apply(lambda x: " ".join([word for word in x.split() if word not in stop_words]))
        movies_df['review_en'] = movies_df['review_en'].apply(lambda x: " ".join([word for word in x.split() if word not in stop_words_e]))

        #Eliminamos las palabras que no pertenecen al Español ni Inglés
        lista_correcciones =  []
        for index, value in movies_df['review_es'].iteritems():
            for word in self.verificar_palabra(value):
                lista_correcciones.append(word)

        movies_df['review_es'] = movies_df['review_es'].apply(lambda x: re.sub(r'\b(' + '|'.join(lista_correcciones) + r')\b', x))
        

        print("Finished preprocessing text...")
        return movies_df