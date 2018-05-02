from flask import Flask, request, render_template
import setup

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
	if request.method == 'POST':
		query = request.form

	return render_template('results.html', query=query)

if __name__ == '__main__':
	app.run(debug = True)
