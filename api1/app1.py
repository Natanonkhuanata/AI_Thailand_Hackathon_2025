from flask import Flask, jsonify
import requests
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route('/')
def hello():
    logging.info("API1: Received request from user.")
    try:
        response = requests.get('http://api2:9999/')
        logging.info(f"API1: Response from API2: {response.text}")
        return jsonify({
            "Api1": "Hello this is API1",
            "Api2_response": response.json()
        })
    except Exception as e:
        logging.error(f"API1: Error calling API2: {e}")
        return jsonify({"error": "API2 not reachable"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)
