from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd
from flask_cors import CORS

app = Flask(__name__, static_folder="../frontend", static_url_path="")
CORS(app)

model = joblib.load("backend/model.pkl")
le = joblib.load("backend/label_encoder.pkl")

@app.route("/")
def home():
    return app.send_static_file("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    df = pd.DataFrame([{
        "sleep_hours": float(data["sleep_hours"]),
        "heart_rate": float(data["heart_rate"]),
        "study_hours": float(data["study_hours"]),
        "screen_time": float(data["screen_time"])
    }])

    prediction = model.predict(df)
    result = le.inverse_transform(prediction)

    return jsonify({"stress_level": result[0]})

if __name__ == "__main__":
    app.run(debug=True)