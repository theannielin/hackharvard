# bobble.py
# Authors: {Annie Lin, Joanne Koong}
# Date: {December 7, 2015}
# Emails: {annielin@college.harvard.edu, joannekoong@college.harvard.edu}
# ----------------
# This is the Bottle web server that our app runs on.

from bottle import route, run, template, static_file
from marky import marky
import json
import os

@route('/static/<filename>')
def static(filename):
    return static_file(filename, root= os.getcwd() + '/static')

# Our homepage
@route('/')
def home(): 
	return template('home.html')

# Server response when a request is sent from homepage
@route('/marks/<sentences:int>/<tag>')
def marks(sentences, tag):
	answer = {}
	answer['answer'] = marky(sentences, tag)
	return json.dumps(answer)

port = os.environ.get('PORT', 5000)
run(host='0.0.0.0', port=port)