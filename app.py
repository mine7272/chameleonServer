from flask import Flask, jsonify
from flask_restx import Api,Resource,reqparse

app = Flask(__name__)

api = Api(app, version='1.0', title='API 문서', description='Swagger 문서', doc="/api-docs")

@app.route('/')
def hello_world():
    return "Test 111"

@app.route('/hihi/<text>')
def hihi(text):
    return jsonify({"hihi":text})
 
if __name__ == "__main__":
    app.run(host='0.0.0.0')

