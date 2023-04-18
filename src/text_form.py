from wtforms import Form
from wtforms import StringField, TextAreaField, DecimalField, SelectField, EmailField, SubmitField
from wtforms import validators


class Text_form(Form):
    texto = TextAreaField('Escribe tu opinión...',[ validators.InputRequired(message='Cuál es tu opinión?!.'),
    validators.length(min=50, max=900, message='No exceda el número de digitos !.')])

    """
     link = StringField('Link de vivienda',[ validators.InputRequired(message='Ingresa el número baños!.')])

    image = StringField('Imagen de la vivienda',[ validators.InputRequired(message='Ingresa la imagen de la casa!.')])

    area = StringField('Área de la casa',[ validators.InputRequired(message='Ingresa el área de la casa!.'), 
    validators.length(min=1, max=10, message='No exceda el número de digitos !.')])
    
    habitaciones = StringField('Habitaciones', [validators.InputRequired(message='Ingresa el número de baños!.'),
    validators.length(min=1, max=10, message='No exceda el número de digitos !.')])
    
    baños = StringField('Baños',[ validators.InputRequired(message='Ingresa el número baños!.'),
    validators.length(min=1, max=10, message='No exceda el número de digitos !.')])

    ciudad = StringField('Ej. Barrio - ciudad',[ validators.InputRequired(message='Ej. Bosa - Bogotá!.'), 
    validators.length(min=1, max=50, message='No exceda el número de digitos !.')])

    """
   