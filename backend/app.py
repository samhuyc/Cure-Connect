from flask import Flask, request, jsonify, render_template
import random

app = Flask(__name__)

df = []

def get_question(df):
    v = random.random()
    if v < 0.5:
        return "this is T/F question", 0
    else:
        return "this is input question", 1

def initial_filter(age, sex, zip, dist):
    df = df 
    return get_question(df)

def continue_filter_bool(response):
    df = df #remove/flag non-applicable trials
    return get_question(df)

def continued_filter_float(response):
    df = df #remove/flag non-applicable trials
    return get_question(df)

# Simulating backend logic to determine response and type based on user input
def process_inputs(landing_input, info_inputs):
    statement = f"Processed data: {landing_input}, {info_inputs}"
    statement_type = random.choice([0, 1])
    return statement, statement_type

# To store user session data (in-memory storage for simplicity)
user_sessions = {}

@app.route('/')
def index():
    return "Server session started."  # Serve the index page

@app.route('/submit_landing', methods=['POST'])
def submit_landing():
    data = request.json # age, sex, location
    question, question_type = initial_filter([])

    return jsonify({'question': question, 'question_type': question_type})

@app.route('/submit_info', methods=['POST'])
def submit_info():
    data = request.json
    user_id = data['user_id']
    info_inputs = data['info_inputs']
    
    # Store info inputs
    user_sessions[user_id]['info_inputs'] = info_inputs

    # Process data to generate response
    statement, statement_type = process_inputs(user_sessions[user_id]['landing_input'], info_inputs)

    return jsonify({'statement': statement, 'statement_type': statement_type})

@app.route('/submit_answer', methods=['POST'])
def submit_answer():
    data = request.json
    user_id = data['user_id']
    answer = data['answer']
    
    # Store the user response and generate the next response
    user_sessions[user_id]['responses'].append(answer)

    if len(user_sessions[user_id]['responses']) >= 10:
        # End the process after 10 responses or backend decision
        result = [{'a': 'value_a', 'b': 'value_b', 'c': 'value_c', 'd': 'value_d'} for _ in range(10)]
        return jsonify({'next': 'result_page', 'result': result})
    
    # Process for the next question
    landing_input = user_sessions[user_id]['landing_input']
    info_inputs = user_sessions[user_id]['info_inputs']
    statement, statement_type = process_inputs(landing_input, info_inputs)

    return jsonify({'statement': statement, 'statement_type': statement_type, 'next': f'type_{statement_type}_page'})

@app.route('/get_result', methods=['GET'])
def get_result():
    user_id = request.args.get('user_id')
    result = user_sessions[user_id]['responses']
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
