import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import accuracy_score, mean_squared_error, f1_score, recall_score
import joblib
import numpy as np

# Load your dataset (replace 'your_dataset.csv' with the actual file path)
df = pd.read_csv("cleaned.csv")

# Preprocessing
# Convert categorical features to numeric using OneHotEncoder
categorical_features = ["Origin", "Destination", "Vehicle Type", "Weather Conditions", "Traffic Conditions"]
encoder = OneHotEncoder()
encoded_features = encoder.fit_transform(df[categorical_features]).toarray()

# Combine encoded features with numerical features
numerical_features = df[["Distance (km)"]].values
X = np.hstack([encoded_features, numerical_features])

# Prepare target variables
y_delayed = df["Delayed"].values
y_difference = df["Delivery Difference (Days)"].values

# Split the dataset
X_train, X_test, y_train_delayed, y_test_delayed = train_test_split(X, y_delayed, test_size=0.2, random_state=42)
_, X_test_diff, _, y_test_difference = train_test_split(X, y_difference, test_size=0.2, random_state=42)

# Logistic Regression for Delayed Prediction
logreg = LogisticRegression()
logreg.fit(X_train, y_train_delayed)

y_pred_delayed = logreg.predict(X_test)

# Metrics for Delayed Prediction
accuracy = accuracy_score(y_test_delayed, y_pred_delayed)
f1 = f1_score(y_test_delayed, y_pred_delayed)
recall = recall_score(y_test_delayed, y_pred_delayed)

print("Accuracy for Delayed Prediction:", accuracy)
print("F1 Score for Delayed Prediction:", f1)
print("Recall for Delayed Prediction:", recall)

# Save the Logistic Regression model
joblib.dump(logreg, "logistic_regression_model.pkl")

# Random Forest Regressor for Delivery Difference Prediction
regressor = RandomForestRegressor(random_state=42)
regressor.fit(X_train, y_train_delayed)  # Using the same training set for simplicity

y_pred_difference = regressor.predict(X_test_diff)

# Metrics for Delivery Difference Prediction
mse = mean_squared_error(y_test_difference, y_pred_difference)
print("MSE for Delivery Difference Prediction:", mse)
# Save the OneHotEncoder for use in the Flask app
joblib.dump(encoder, "encoder.pkl")


# Save the Random Forest Regressor model
joblib.dump(regressor, "random_forest_regressor_model.pkl")
