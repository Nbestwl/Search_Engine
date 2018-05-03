from flask import Flask, request, render_template
from engine_core import search, read_data
# from engine_core.linkedList import LinkedList
import unicodedata

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
	# if the user inputs a query, grab the query and feed in to the search method to calulate similarity score
	if request.method == 'POST':
		query = request.form['search_query']

		# convert unicode to string
		query = unicodedata.normalize('NFKD', query).encode('ascii','ignore')
		# calculate cosine similarity between files and query
		scores = search(query)

 		return render_template("results.html", scores=scores)

if __name__ == '__main__':
	app.run(debug = True)
