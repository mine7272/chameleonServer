from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Test 111"

@app.route('/hihi/<text>')
def hihi(text):
    return jsonify({"hihi":text})
 
if __name__ == "__main__":
    app.run(host='0.0.0.0')

