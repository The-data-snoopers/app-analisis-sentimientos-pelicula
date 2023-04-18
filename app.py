from flask import Flask, redirect, url_for
import os
from dotenv import load_dotenv
from src.views import prediccion


load_dotenv()


app = Flask(__name__)


@app.route('/')
def principal():
    return redirect(url_for('prediccion.crear_prediccion'))


app.register_blueprint(prediccion, url_prefix='/')

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)



