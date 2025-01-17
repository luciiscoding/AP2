import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

file_path = "tourism_dataset.csv"
if not os.path.exists(file_path):
    raise FileNotFoundError(f"Fișierul {file_path} nu a fost găsit.")

data = pd.read_csv(file_path)

X = data[['Accommodation_Available', 'Category', 'Country', 'Rating', 'Visitors']] 
y = data['Revenue'] 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


pipeline = Pipeline(steps=[
    ('preprocessor', ColumnTransformer(
        transformers=[
            ('num', SimpleImputer(strategy='mean'), ['Rating', 'Visitors']),
            ('cat', OneHotEncoder(), ['Accommodation_Available', 'Category', 'Country'])  
        ])),
    ('regressor', LinearRegression())  
])

pipeline.fit(X_train, y_train)

y_pred = pipeline.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

print("Performanța fiecărui model (MSE):")
results = {'Linear Regression': mse}
for model_name, mse in results.items():
    print(f"{model_name}: {mse:.4f}")

#selectam cel mai bun model
best_model = min(results, key=results.get)
print(f"Cel mai bun model este {best_model} cu MSE: {results[best_model]:.4f}")