from flask import Flask, render_template, jsonify
from flask import request
from crawling import crawling

app = Flask(__name__)

@app.route('/')
def youtube():
    return render_template('youtube.html')

@app.route('/crawtub', methods=[''])
def crawYtub():
    return

if __name__=="__main__":
    app.run(debug=True, host="127.0.0.1", port="5000")