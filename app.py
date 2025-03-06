from flask import Flask, jsonify, request
import pandas as pd
from flask import render_template
import joblib

app = Flask(__name__)

# Load the dataset
df = pd.read_csv('car_price_dataset.csv')

# Load the trained model by using .csv
model = joblib.load('car_price_model.pkl')

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Get all cars
@app.route('/cars', methods=['GET'])
def get_all_cars():
    return jsonify(df.to_dict(orient='records'))

# Get cars by brand
@app.route('/cars/brand/<string:brand>', methods=['GET'])
def get_cars_by_brand(brand):
    filtered_cars = df[df['Brand'].str.lower() == brand.lower()]
    return jsonify(filtered_cars.to_dict(orient='records'))

# Get cars by price range
@app.route('/cars/price', methods=['GET'])
def get_cars_by_price_range():
    min_price = request.args.get('min', default=0, type=float)
    max_price = request.args.get('max', default=float('inf'), type=float)
    filtered_cars = df[(df['Price'] >= min_price) & (df['Price'] <= max_price)]
    return jsonify(filtered_cars.to_dict(orient='records'))

# Add a new car (for demonstration purposes)
@app.route('/cars/add', methods=['POST'])
def add_car():
    new_car = request.json
    df.loc[len(df)] = new_car
    return jsonify({"message": "Car added successfully!", "car": new_car}), 201

# Predict car price
@app.route('/predict', methods=['POST'])
def predict():
    # Get the input data from the request
    input_data = request.json

    # Convert the input data into a DataFrame
    input_df = pd.DataFrame([input_data])

    # Make a prediction
    prediction = model.predict(input_df)

    # Return the prediction as JSON
    return jsonify({"predicted_price": prediction[0]})

# Run the app
if __name__ == '__main__':
    app.run(debug=True)