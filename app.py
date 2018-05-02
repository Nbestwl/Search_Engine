from flask import Flask, request, render_template
from engine_core import search, read_data
from engine_core.linkedList import LinkedList

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST','GET'])
def results():
	# if the user inputs a query, grab the query and feed in to the search method to calulate similarity score
	if request.method == 'POST':
		result = request.form
		search(result)

 		return render_template("results.html",result = result)

if __name__ == '__main__':
	app.run(debug = True)
