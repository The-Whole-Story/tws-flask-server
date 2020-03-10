from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '''
    <h1>Hello World!</h1>
    <h3>from: The Whole Story</h3>
    <p>You'll know us soon :)</p>
    '''