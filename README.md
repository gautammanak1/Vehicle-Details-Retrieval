# Vehicle Details



## Prerequisites

- Python 3.8 or higher
- `requests` library
- `uagents` library

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/gautammanak1/Vehicle-Details-Retrieval.git
    cd Vehicle-Details-Retrieval
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
    python vehicleAgent.py
    ```



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
