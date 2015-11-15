from bottle import route, run, template, static_file
from marky import marky
import json


@route('/static/<filename>')
def static(filename):
    return static_file(filename, root='/Users/Joanne/Documents/hackharvard/static')

@route('/')
def home(): 
	return template('home.html')

@route('/marks')
def marks():
	answer = {}
	answer['answer'] = marky(5, 'ocaml')
	return json.dumps(answer)

run(host='localhost', port=8080, debug=True)


