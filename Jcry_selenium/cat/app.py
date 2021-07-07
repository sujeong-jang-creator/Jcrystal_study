from flask import Flask, render_template, jsonify
from flask import request
from downcat import download
# from crawcat import crawcat

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/crawcat', methods=['post'])
# def test():
#     cats = crawcat()
#     return jsonify(cats)

@app.route('/downcat', methods=['post'])
def test():
    cats = crawcat()
    return jsonify(cats)

if __name__=="__main__":
    app.run(debug=True, host="127.0.0.1", port="5000")