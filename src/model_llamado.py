from joblib import load
import dill
import pickle as pkl
from pipeline.Cargar_modelo import Cargar_modelo 
import pandas as pd

async llamar_modelo(df : pd.DataFrame):
    global prediction_model
    

    modelo = Cargar_modelo(df.columns)
    result = modelo.make_predictions(df)
    return result
