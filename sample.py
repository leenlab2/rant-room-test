# main.py
from flask import Flask
from flask import url_for, render_template, request
from test_database import insert_user_message

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/foo', methods=['POST'])
def foo():
    return insert_user_message(thoughts=request.form['thoughts'])


if __name__ == "__main__":
    app.run(port=8080, debug=True)
