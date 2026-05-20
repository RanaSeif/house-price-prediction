import joblib

model = joblib.load("model.pkl")

size = float(input("Enter house size: "))

prediction = model.predict([[size]])

print("Predicted price:", prediction[0])