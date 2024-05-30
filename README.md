# Vehicle Details and Payment Agent System

This project demonstrates a decentralized agent-based system where two agents, Alice and Bob, interact to fetch vehicle details from an API and process payments using a blockchain network. The agents are built using the `uagents` framework and interact via a `Bureau` that facilitates communication between them.

## Features

- Alice requests vehicle details from Bob.
- Bob fetches the vehicle details using the specified API.
- Alice requests payment from Bob.
- Bob processes the payment and sends a transaction confirmation back to Alice.

## Prerequisites

- Python 3.8 or higher
- `requests` library
- `uagents` library

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/your-username/vehicle-details-payment-agent.git
    cd vehicle-details-payment-agent
    ```

2. **Install the required libraries**:
    ```sh
    pip install requests
    pip install uagents
    ```

## Usage

1. **Configure the Agents**:
   Update the `vehicle_number` and `rapidapi_key` variables in the `request_vehicle_details` function within the code. Replace the example values with actual values.

2. **Run the Agents**:
    ```sh
    python main.py
    ```

## Code Explanation

### Agent Setup

Two agents are set up with predefined seed phrases:
- **Alice**: Requests vehicle details and payment.
- **Bob**: Fetches vehicle details and processes payment.

### Vehicle Details Fetching

- **Alice**: Periodically sends a vehicle details request to Bob.
- **Bob**: Receives the request, fetches the vehicle details from the API, and sends the details back to Alice.

### Payment Processing

- **Alice**: Periodically requests funds from Bob.
- **Bob**: Receives the payment request, processes the transaction, and sends the transaction info back to Alice.
- **Alice**: Confirms the transaction upon receiving the transaction info.

### API Integration

The `get_vehicle_details` function uses the `requests` library to interact with the vehicle information API:

```python
def get_vehicle_details(vehicle_number, rapidapi_key):
    url = "https://rto-vehicle-information-verification-india.p.rapidapi.com/api/v1/rc/vehicleinfo"
    
    payload = {
        "reg_no": vehicle_number,
        "consent": "Y",
        "consent_text": "I hereby declare my consent agreement for fetching my information via AITAN Labs API"
    }
    
    headers = {
        'content-type': "application/json",
        'X-RapidAPI-Key': rapidapi_key,
        'X-RapidAPI-Host': "rto-vehicle-information-verification-india.p.rapidapi.com"
    }
    
    response = requests.post(url, json=payload, headers=headers)
    
    return response.text
