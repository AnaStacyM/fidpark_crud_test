import requests
import pytest

BASE_URL = "https://demo1.fidpark.com/api"
AUTH = ("demo", "Demo12345")
HEADERS = {"Content-Type": "application/json"}

# Sample data for creating a client
client_data = {
    "name": "Test Client",
    "email": "testclient@example.com",
    "phone": "1234567890"
}

@pytest.fixture(scope="module")
def client_id():
    # Create client
    response = requests.post(f"{BASE_URL}/clients", json=client_data, auth=AUTH, headers=HEADERS)
    assert response.status_code in [200, 201]
    client = response.json()
    yield client["id"]

    # Delete client after test
    requests.delete(f"{BASE_URL}/clients/{client['id']}", auth=AUTH)

def test_read_client(client_id):
    # Read client by ID
    response = requests.get(f"{BASE_URL}/clients/{client_id}", auth=AUTH)
    assert response.status_code == 200
    client = response.json()
    assert client["name"] == client_data["name"]

def test_update_client(client_id):
    # Update client data
    updated_data = {"phone": "0987654321"}
    response = requests.put(f"{BASE_URL}/clients/{client_id}", json=updated_data, auth=AUTH, headers=HEADERS)
    assert response.status_code in [200, 204]

    # Verify update
    response = requests.get(f"{BASE_URL}/clients/{client_id}", auth=AUTH)
    client = response.json()
    assert client["phone"] == updated_data["phone"]
