from flask import Flask
from resources import places
import models 
from flask_cors import CORS 

DEBUG=True
PORT=8000

app = Flask(__name__)




@app.route('/')
def index():
 	return 'Hello'








if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT)