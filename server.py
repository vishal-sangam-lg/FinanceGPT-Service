from flask import Flask, render_template, request, jsonify
from main import get_response_from_bot
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route('/')
def home():
    return "<h1>Server is Up!</h1>"


@app.route('/bot-response', methods=["POST"])
def api():
    if request.method == 'POST':
        body = request.json
        if 'prompt' in body:
            print("Request received: " + body['prompt'])
            response = get_response_from_bot(body['prompt'])
            print(jsonify({"bot_response": response}))
            return jsonify({"bot_response": response})
        else:
            return jsonify({'Error': 'Unprocessable Entity: prompt is required field in the body of request'}), 422


# Only for dev
# if __name__ == "__main__":
#     app.run(host="localhost", port=9000, debug=True)
