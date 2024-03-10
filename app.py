from flask import Flask, render_template, jsonify
from flask_cors import CORS
from chatbot import get_chat_response

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/style.css')
def style():
    return app.send_static_file('style.css')

@app.route('/script.js')
def script():
    return app.send_static_file('script.css')

@app.route('/get_response/<user_input>')
def get_response(user_input):
    response = get_chat_response(user_input)
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
