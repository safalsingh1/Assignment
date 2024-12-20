from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load the saved models and encoder
logistic_model = joblib.load("logistic_regression_model.pkl")
regressor_model = joblib.load("random_forest_regressor_model.pkl")
encoder = joblib.load("encoder.pkl")

# Define categorical feature order
categorical_features = ["Origin", "Destination", "Vehicle Type", "Weather Conditions", "Traffic Conditions"]

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        origin = request.form.get("origin")
        destination = request.form.get("destination")
        vehicle_type = request.form.get("vehicle_type")
        weather = request.form.get("weather_conditions")
        traffic = request.form.get("traffic_conditions")
        distance = float(request.form.get("distance"))

        # Encode categorical features
        input_features = [[origin, destination, vehicle_type, weather, traffic]]
        encoded_features = encoder.transform(input_features).toarray()

        # Combine encoded features with numerical distance
        final_features = np.hstack([encoded_features, [[distance]]])

        # Make predictions
        delay_prediction = logistic_model.predict(final_features)[0]
        delivery_difference = regressor_model.predict(final_features)[0]

        # Map delay prediction to Yes/No
        delay_result = "Yes" if delay_prediction == 1 else "No"

        return render_template(
            "result.html",
            delay_result=delay_result,
            delivery_difference=round(delivery_difference, 2)
        )
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    app.run(debug=True)
