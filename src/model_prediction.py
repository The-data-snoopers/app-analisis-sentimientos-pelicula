from joblib import load
import pickle as pkl
from pipeline.Preprocessor import Preprocessor

class Model:

    def __init__(self):
        #self.model = pkl.load(open('src/assets/pipeline_peliculas.pkl', 'rb'))
        self.model = load('src/assets/pipeline_peliculas.joblib')
    
    def make_predictions(self, data):
        result = self.model.predict(data)
        return result
