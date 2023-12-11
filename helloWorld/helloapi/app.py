from flask import Flask, request, Response, jsonify
import main
import json
from optimizer import opt

app = Flask(__name__)

@app.route('/')
def index():

    result={"status":'ok'}
    return jsonify(result)

@app.route('/health', methods=['GET'])
def health_check():
    return Response(response=json.dumps({"status": 'healthy'}), status=200, mimetype="application/json")

@app.route('/predict', methods=['POST'])
def process_json():
    content_type = request.headers.get('Content-Type')
    req = request.get_json()
    res, choice = main.main(req)
    # res = opt(req)
    response = {"predictions": [{choice: [res]}]}
    return response


@app.route('/baseline', methods=['POST'])
def baseline_json():
    content_type = request.headers.get('Content-Type')
    json = request.json
    print(json)
    response = {"response": [{"scores": [0.989, 0.761]}]}

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)