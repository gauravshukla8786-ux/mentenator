from flask import Flask, render_template, request
import json
import random

app = Flask(__name__)

# Load responses from JSON file
with open('responses.json', 'r') as file:
    responses = json.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get', methods=['GET'])
def get_bot_response():
    user_input = request.args.get('msg').lower()

    # Basic NLP: match keywords to responses
    for keyword in responses:
        if keyword in user_input:
            possible_replies = responses[keyword]
            if isinstance(possible_replies, list):
                return random.choice(possible_replies)
            else:
                return possible_replies

    # Default fallback
    return random.choice([
        "I'm here to listen. Tell me more.",
        "Please go on, I'm listening.",
        "That sounds tough. Want to talk more?",
        "Hmm, I understand. Feel free to share anything."
    ])

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
    
