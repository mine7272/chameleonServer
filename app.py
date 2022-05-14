import os
import subprocess
from urllib import response
from flask import Flask, request, jsonify, json
from flask_cors import CORS
from flask_restx import Api, Resource, reqparse
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = '../database'

@app.errorhandler(404)
def page_not_found(error):
     return jsonify({"result": "fail"}), 404

@app.route('/server-test')
def home():
    return jsonify({"result": "ok"})

@app.route('/file/upload', methods = ['GET', 'POST'])
def upload_file():
    if 'file' not in request.files:
            return jsonify({"result": "fail"})
    f = request.files['file']
    onlynum=request.headers.get('authorization')
    os.makedirs("../database/"+onlynum)
    f.save("../database/{}/".format(onlynum) +secure_filename(f.filename))
    return jsonify({"result":"ok"})
     
@app.route('/faces', methods = ['GET', 'POST'])
def faces():
    if request.method == 'GET':
        onlynum=request.headers.get('authorization')
        os.system("cd ../ && python src/classifier.py --type photo --key "+onlynum)

     
@app.route('/version', methods = ['GET'])
def version():
    return jsonify({
        "result": "ok",
        "message": "0.0.1"
    })
    

if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=5000,debug=1)
