import pytest
from app import app  # Import your Flask app


@pytest.fixture
def client():
    # Create a test client for the Flask app
    with app.test_client() as client:
        yield client


# Ensure there are two blank lines before the function definition
def test_predict_endpoint(client):
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
    response = client.post('/predict', json=data)

    # Check the response status code
    assert response.status_code == 200

    # Check the response content
    response_data = response.get_json()
    assert "predicted_price" in response_data
    assert isinstance(response_data["predicted_price"], float)