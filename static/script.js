// Add Car Form Submission
document.getElementById('addCarForm').addEventListener('submit', function (e) {
    e.preventDefault();

    const formData = new FormData(this);
    const data = Object.fromEntries(formData.entries());

    fetch('/cars/add', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
        .then(response => response.json())
        .then(data => {
            document.getElementById('addCarResponse').innerText = data.message;
        })
        .catch(error => {
            console.error('Error:', error);
        });
});

// Predict Price Form Submission
document.getElementById('predictPriceForm').addEventListener('submit', function (e) {
    e.preventDefault();

    const formData = new FormData(this);
    const data = Object.fromEntries(formData.entries());

    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
        .then(response => response.json())
        .then(data => {
            document.getElementById('predictPriceResponse').innerText = `Predicted Price: $${data.predicted_price.toFixed(2)}`;
        })
        .catch(error => {
            console.error('Error:', error);
        });
});