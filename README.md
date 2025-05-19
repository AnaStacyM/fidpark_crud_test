# FidPark API - Automated CRUD Test (Clients)

## Overview
This repository contains automated tests to verify CRUD operations on the `Clients` object in the FidPark system using its public API.

## Requirements
- Python 3.7+
- pip

## Installation
Clone the repository and install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Tests

```bash
pytest test_fidpark_clients.py
```

## Credentials
- API URL: https://demo1.fidpark.com/swagger/index.html
- Username: `demo`
- Password: `Demo12345`

## Test Coverage
- ✅ Create a new client
- ✅ Retrieve client by ID
- ✅ Update client data
- ✅ Delete client after test

## Author
Anastasia Metelitsa
Email: ametelica20@gmail.com
GitHub: https://github.com/AnaStacyM

## Notes
This project is for demonstration and testing purposes only.

Make sure to clean up any test data if using real environments.
