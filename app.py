import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_restx import Api, Resource, reqparse
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = '/'

@app.route('/server-test')
def home():
    return jsonify({"result": "ok"})

@app.route('/file/upload', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return jsonify({"result": "upload success"})
    else :
        return jsonify({"result": "upload fail"})

if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=5000)
