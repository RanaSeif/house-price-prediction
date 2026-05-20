import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

data = {
    size [50, 60, 80, 100, 120, 150, 200],
    price [150, 180, 240, 300, 360, 450, 600]
}

df = pd.DataFrame(data)

X = df[[size]]
y = df[price]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LinearRegression()
model.fit(X_train, y_train)

joblib.dump(model, model.pkl)

print(Model trained successfully!)