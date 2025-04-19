from flask import Flask, render_template, request
from model_setup import search_faq

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        query = request.form['query']
        result = search_faq(query)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)