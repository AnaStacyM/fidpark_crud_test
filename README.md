## FidPark API Automated CRUD Test (Clients)

## Overview

This repository contains automated tests to verify CRUD operations on the Clients object in the FidPark system using its public API.

## Requirements

Python 3.7+

pip

## Installation

Clone the repository and install dependencies:

```git clone https://github.com/AnaStacyM/fidpark_crud_test.git
cd fidpark_crud_test
pip install -r requirements.txt```

## Running the Tests

To execute the test suite:

pytest test_fidpark_clients.py

## Credentials

API URL: https://demo1.fidpark.com/swagger/index.html

Username: demo

Password: Demo12345

## Test Coverage

The test suite includes the following steps:

Create a new client

Retrieve client by ID

Update client data

Delete client after test (cleanup)

## Output

After running, pytest will display the result for each test:

test_fidpark_clients.py::test_read_client PASSED
test_fidpark_clients.py::test_update_client PASSED

## Author

Anastasia Metelitsa
📧 Email: ametelica20@gmail.com
🌐 GitHub: AnaStacyM

## Notes

This project is for demonstration and testing purposes only. Please clean up any test data when using real environments.
