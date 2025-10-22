from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    if request.method == 'GET':
        response = {
            "message": "Hello, I am running inside a Docker container! 🚀",
            "status": "success",
            "method": "GET"
        }
        return jsonify(response), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)