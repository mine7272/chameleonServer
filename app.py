import os
from flask import Flask, request
from flask_cors import CORS
from flask_restx import Api, Resource, reqparse
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = '/'

@app.route('/')
def home():
    return 'test'

@app.route('/fileupload', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return '파일 업로드 성공!'

if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=5000)
