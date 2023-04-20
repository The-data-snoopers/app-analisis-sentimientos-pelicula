from flask import Blueprint, request, render_template, abort, redirect, url_for
import pandas as pd
import numpy as np
from joblib import load
from src.text_form import Text_form
from src.models import Comentario
import pickle as pkl
from src.model_prediction import Model



prediccion = Blueprint('prediccion', __name__, template_folder='./templates')


@prediccion.route("/predecir", methods=['GET', 'POST'])
def crear_prediccion():

    formulario = Text_form(request.form)
    if request.method == 'GET':
        return render_template('index.html', formulario=formulario)
        
    if request.method == 'POST' and formulario.validate():
        texto = formulario.texto.data
        print("texto: ", texto)
       

        texto = Comentario( comentario=texto)

        df = pd.DataFrame(texto.dict(), columns=texto.dict().keys(), index=[0])
        """
        model = load("src/pipeline_peliculas.joblib")
        result = model.predict(df)
        """
    
        modelo = Model()
        result = modelo.make_predictions(df)
        
        res =  np.round(result[0], 5),
        resultado_modelo = int(res[0])
        print("resultado prediccion: ", resultado_modelo)
        return render_template('index.html', formulario=formulario, result=resultado_modelo)

    else:
      
        return render_template('index.html', formulario=formulario)
    