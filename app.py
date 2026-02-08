from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Football AI Predictor is running successfully 🚀"

@app.route("/predict")
def predict():
    return jsonify({
        "league": "All Leagues",
        "match": "Team A vs Team B",
        "prediction": "Over 2.5 Goals",
        "confidence": "72%"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
