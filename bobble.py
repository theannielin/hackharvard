from bottle import route, run
from marky import marky

@route('/marks')
def marks():
    return marky(5, 'ocaml')

run(host='localhost', port=8080, debug=True)