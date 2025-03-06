import requests


# Base URL of the Flask app
BASE_URL = "http://127.0.0.1:5000"


def test_predict_endpoint():
    # Test data
    data = {
        "Brand": "Toyota",
        "Model": "Corolla",
        "Year": 2021,
        "Engine_Size": 2.0,
        "Fuel_Type": "Petrol",
        "Transmission": "Automatic",
        "Mileage": 15000,
        "Doors": 4,
        "Owner_Count": 1
    }

    # Send a POST request to the /predict endpoint
    response = requests.post(f"{BASE_URL}/predict", json=data)

    # Check the response status code
    assert response.status_code == 200

    # Check the response content
    response_data = response.json()
    assert "predicted_price" in response_data
    assert isinstance(response_data["predicted_price"], float)
