from bottle import route, run, template, static_file
from marky import marky
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
	answer['answer'] = marky(sentences, tag)
	return json.dumps(answer)

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))


