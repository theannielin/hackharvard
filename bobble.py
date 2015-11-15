from bottle import route, run
from marky import marky
import json

@route('/marks')
def marks():
	answer = {}
	answer['answer'] = marky(5, 'ocaml')
	return json.dumps(answer)

run(host='localhost', port=8080, debug=True)