from flask import Flask
import os
from dotenv import load_dotenv

load_dotenv()


app = Flask(__name__)




@app.route('/')
def favicon():
    return "Hola mundo, tenemos un servidor funcionando"


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)



