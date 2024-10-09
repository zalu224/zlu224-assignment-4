from flask import Flask, render_template, request, jsonify
from lsa import LatentSemanticAnalyzer
import numpy as np

app = Flask(__name__)

# Initialize the LSA model
lsa_model = LatentSemanticAnalyzer()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    results, similarities = lsa_model.search(query)
    
    # Convert NumPy arrays to Python lists for JSON serialization
    results_list = results  # results are already in list form
    similarities_list = similarities.tolist()  # Convert NumPy array to list
    
    # Send back results and similarities for the visualization
    return jsonify({
        'results': results_list,  # Top 5 documents
        'similarities': similarities_list  # Similarity scores as a list
    })

if __name__ == '__main__':
    app.run(port=3000, debug=True)
