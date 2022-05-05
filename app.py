import os
from urllib import response
from flask import Flask, request, jsonify, json
from flask_cors import CORS
from flask_restx import Api, Resource, reqparse
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = '/'

api =Api(app, version='1.0', title='API 문서', description='Swagger 문서', doc="/api-docs")
test_api = api.namespace('test', description='조회 API')



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
    
@app.route('/test', methods = ['POST'])
def upload_test():
    jsonData=request.args.get('message')
    print(jsonData)
    return {
        "result": "ok",
        "message": "request"
    }
    

if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=5000 , debug="True")
