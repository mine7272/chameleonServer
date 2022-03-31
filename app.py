from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Test 111"
 
@app.route('/userLogin', methods = ['POST'])
def userLogin():
    user = request.get_json()#json 데이터를 받아옴
    return jsonify(user)# 받아온 데이터를 다시 전송
 
@app.route('/hihi/<text>')
def hihi(text):
    return jsonify({"hihi":text})
 
 
if __name__ == "__main__":
    app.run()

app.run(host='0.0.0.0', port=80)