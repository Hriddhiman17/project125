from flask import Flask, jsonify, request
from classifier import get_prediction
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)

@app.route("/")
def home():
  return "Home Page"

@app.route ("/predict-alphabet", methods=["POST"])
def predict_data():
    image = request.files.get("alphabet")
    prediction = get_prediction(image)

    return jsonify ({ "prediction": prediction }), 200

if __name__ == "__main__":
    app.run(debug=True)
