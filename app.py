from flask import Flask, render_template, request, jsonify
from flask_ngrok import run_with_ngrok

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Test 2"

run_with_ngrok(app)
app.run()