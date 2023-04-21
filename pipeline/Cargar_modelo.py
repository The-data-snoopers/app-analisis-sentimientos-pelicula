from joblib import load
import dill
import pickle as pkl
from pipeline.A import A
#from pipeline.A import Preprocessor
class Cargar_modelo:

    def __init__(self, columns):
        
        #with open('./pipeline/pipeline_peliculas.joblib', 'rb') as file:
        #    self.model = pkl.load(file=file)
    
        self.model = load('./pipeline/pipeline_peliculas.joblib')
    
    def make_predictions(self, data):
        result = self.model.predict([data])
        return result
