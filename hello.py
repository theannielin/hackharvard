# import os
# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def hello():
#     return 'Hello World!'
import json
import os
from flask import Flask

app = Flask(__name__)


# @app.route('/static/<filename>')
# def static(filename):
#     return static_file(filename, root= os.getcwd() + '/static')

@app.route('/')
def home(): 
	return template('home.html')

# @app.route('/marks/<sentences:int>/<tag>')
# def marks(sentences, tag):
# 	answer = {}
# 	answer['answer'] = marky(sentences, tag)
# 	return json.dumps(answer)