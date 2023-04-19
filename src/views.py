from flask import Blueprint, request, jsonify, render_template, abort, redirect, url_for
import pandas as pd
import numpy as np
from joblib import load
from src.text_form import Text_form
from src.models import Comentario


prediccion = Blueprint('prediccion', __name__, template_folder='./templates')


@prediccion.route("/predecir", methods=['GET', 'POST'])
def crear_prediccion():

    formulario = Text_form(request.form)
    if request.method == 'GET':
        return render_template('index.html', formulario=formulario)
        
    if request.method == 'POST' and formulario.validate():
        texto = formulario.texto.data
        print("texto: ", texto)
        return render_template('index.html', formulario=formulario, result="A la persona le gusta la pelicula")
        ## pasar datos al model
        
        
        prediccion = Comentario( area=texto)

        df = pd.DataFrame(prediccion.dict(), columns=prediccion.dict().keys(), index=[0])

        model = load("src/assets/model.joblib")
        result = model.predict(df)
        res =  np.round(result[0], 5),
        return res
        #print("resultado prediccion: ", result)

    else:
      
        return render_template('index.html', formulario=formulario)
    