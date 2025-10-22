from flask import Flask, jsonify, request
import logging

app = Flask(__name__)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


@app.route('/', methods=['GET'])
def home():
    if request.method == 'GET':
        response = {
            "message": "Hello, I am running inside a Docker container! 🚀",
            "status": "success",
            "method": "GET"
        }
        logger.info(f"Endpoint '/' called. Response: {response}")
        return jsonify(response), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)