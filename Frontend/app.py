from flask import render_template
from flask_cors import CORS
from flask import Flask

app = Flask(__name__)

@app.route('/')
def base():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
    CORS(app)