from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/first_question", methods=["POST"])
def hello_world():
    # Get the data from the request
    # data = request.get_json()
    # Return a JSON response
    data = {"question": "What is your blood pressure?", "question_type": True}
    response = jsonify(data)
    return jsonify(data)