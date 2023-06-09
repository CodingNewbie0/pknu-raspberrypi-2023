# Flask 웹서버
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/') # http://localhost:8000/
def index():
    return 'Hello, Flask!!'

if __name__ == '__main__':
    app.run(host='locallhost', port='8000', debug=True)