from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
import random
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
	if not session.get('gold') >=0:
		session['gold'] = 0
	return render_template('index.html')

@app.route('/process_money', methods=['post'])
def guess():
	if not session.get('z'):
		session['z'] = []
	if request.form['building'] == "farm":
		x = random.randrange(11,21)
		session['gold'] += x
		y = "Earned {} gold from the farm!".format(x)
		session['z'].extend([y])
	elif request.form['building'] == "cave":
		x = random.randrange(4,11)
		session['gold'] += x
		y = "Earned {} gold from the cave!".format(x)
		session['z'].extend([y])
	elif request.form['building'] == "house":
		x = random.randrange(1,6)
		session['gold'] += x
		y = "Earned {} gold from the house!".format(x)
		session['z'].extend([y])
	else:
		x = random.randrange(-51,51)
		session['gold'] += x
		y = "Earned {} gold from the casino!".format(x)
		session['z'].extend([y])
	return redirect('/',)

@app.route('/reset')
def reset():
	session.clear()
	return redirect('/')
app.run(debug=True)
