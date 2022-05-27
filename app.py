from flask import Flask, jsonify, request
from predict import predict_penguin
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/predict", methods=["POST"])
def make_prediction():
    penguin = request.json
    return jsonify({"prediction": predict_penguin(penguin)})


if __name__ == "__main__":
    app.run(debug=True)
