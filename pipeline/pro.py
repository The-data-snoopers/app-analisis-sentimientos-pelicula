import pandas as pd
import matplotlib.pyplot as plt
import nltk
import enchant
import pickle as pkl
from joblib import dump, load
import re
from collections import Counter
from nltk.corpus import stopwords
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import FunctionTransformer
from nltk.tokenize import TweetTokenizer
from sklearn.metrics import f1_score, precision_score, recall_score, confusion_matrix, ConfusionMatrixDisplay
from A import A



# Cargar los datos en un DataFrame de pandas
movies_df = pd.read_csv('pipeline/data/MovieReviews.csv', sep=',', encoding="utf-8", index_col=0)


# Función para tokenizar los tweets
nltk.download('punkt')
def tokenizer(text):
    tt = TweetTokenizer()
    return tt.tokenize(text)

# Descargando las stopwords
nltk.download('stopwords')
stop_words_complete = list(stopwords.words('spanish')) + list(stopwords.words('english'))


# Crear el pipeline
text_pipeline = Pipeline([
    ('preprocessing', A()),
    ('vectorizer', CountVectorizer(tokenizer=tokenizer, stop_words=stop_words_complete, lowercase=True)),
    ('classifier', RandomForestClassifier(random_state=2, n_estimators=200, min_samples_split=4, max_depth=3, criterion='entropy'))
])


# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(movies_df['review_es'], movies_df['sentimiento'], test_size=0.2, random_state=42)


# Ajustar el pipeline a los datos de entrenamiento
text_pipeline.fit(X_train, y_train)
print("Pipeline fitted- paso por aquí...")

pipeline_path =  "./pipeline/pipeline_peliculas.joblib"
dump(text_pipeline, pipeline_path)

pipeline_path =  "./pipeline/pipeline_peliculas.pkl"
with open(pipeline_path, 'wb') as file:
    pkl.dump(text_pipeline, file)