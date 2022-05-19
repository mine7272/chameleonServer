from glob import glob
import os,sys
import shutil
import subprocess
from urllib import response
from time import sleep
from concurrent.futures import ThreadPoolExecutor
from flask import Flask, request, jsonify, json
from collections import OrderedDict
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
    if os.path.exists("../database/"+onlynum):
        shutil.rmtree("../database/"+onlynum)
        os.makedirs("../database/"+onlynum)
        f.save("../database/{}/".format(onlynum) +secure_filename(f.filename))
    else :
        os.makedirs("../database/"+onlynum)
        f.save("../database/{}/".format(onlynum) +secure_filename(f.filename))

    return jsonify({"result":"ok"})

@app.route('/file/download', methods = ['GET'])
def download_file():
    
    onlynum=request.headers.get('authorization')
    
    file_list = os.listdir("static/{}/".format(onlynum))
    download_list = [file for file in file_list if file.endswith(".jpg") or file.endswith(".mp4") or file.endswith(".png")]
    
    download_json=OrderedDict()
    download_json["result"]="ok"
    download_json["message"]="파일 다운로드"
    download_json["data"]="http://118.91.7.160/static/{}/{}".format(onlynum,download_list[0])
    
    
    return (json.dumps(download_json,ensure_ascii=False,indent="\t"))

@app.route('/file/delete', methods = ['POST'])
def delete_file():
    onlynum=request.headers.get('authorization')
    if os.path.exists("../database/"+onlynum):
        shutil.rmtree("../database/"+onlynum)
        shutil.rmtree("static/"+onlynum)
    
    return (jsonify({"result":"ok"}))

@app.route('/faces', methods = ['GET', 'POST'])

def faces():
    executor.submit(crop_task)

    if request.method == 'GET':
        onlynum=request.headers.get('authorization')
        #if os.path.exists("static/{}/LQ_faces".format(onlynum)):
        files = os.listdir("static/{}/LQ_faces".format(onlynum))
        
        savedjson=open("static/{}/return1-{}.json".format(onlynum,onlynum))
        savedjson_dict=json.load(savedjson)
        data=savedjson_dict.get("data")

        #json에 줄 data 배열 가공
        for x in range(0,len(data)):
            data[x]["url"]="http://118.91.7.160/"+data[x]['img'][16:]
            data[x]["name"]=data[x]['img'][-7:]
            data[x].pop("img")
            data[x]["gender"]="gender_test"
            data[x]["percent"]=0
    
        face_json=OrderedDict()
        face_json["result"]="ok"
        face_json["message"]="complete"
        face_json["data"]=data
        
        return (json.dumps(face_json,ensure_ascii=False,indent="\t"))
    
    if request.method == 'POST':
        onlynum=request.headers.get('authorization')
        faceindex = request.get_json()
        mode=faceindex.pop("mode")
        with open('static/{}/choice_{}.json'.format(onlynum,onlynum), 'w') as outfile:
           json.dump(faceindex, outfile, indent=4)
        #if mode == 0 :
        os.system("cd ../ && python src/swapper.py --type photo --key "+onlynum)
        #elif mode == 1 :
        #    os.system("cd ../ && python src/swapper.py --type photo --key {} --opt mosaic".format(onlynum))
        #elif mode == 2 :
        #    os.system("cd ../ && python src/swapper.py --type photo --key {} --opt swap_mosaic".format(onlynum))
    return jsonify({"result":"ok"})

def crop_task():
    os.system("cd ../ && python src/classifier.py --type photo --key "+onlynum)
    return jsonify({"result" : "ok","message" : "in progress"})


@app.route('/version', methods = ['GET'])
def version():
    return jsonify({
        "result": "ok",
        "message": "0.0.1"
    })
    

if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=5000,debug=1)
