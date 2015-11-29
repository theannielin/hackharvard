from bottle import route, run, template, static_file
from marky2 import marky2
import json
import os


@route('/static/<filename>')
def static(filename):
    return static_file(filename, root= os.getcwd() + '/static')

@route('/')
def home(): 
	return template('home.html')

@route('/marks/<sentences:int>/<tag>')
def marks(sentences, tag):
	answer = {}
	answer['answer'] = marky2(sentences, tag)
	return json.dumps(answer)

port = os.environ.get('PORT', 5000)
run(host='0.0.0.0', port=port)



